import os
import csv
from app.models import *

# def import_csv_data(db):
#     table_csv_mapping = {
#         Master: 'imports/Master.csv'
#         # Cart: 'extra/imports/Cart.csv',
#         # CartProduct: 'extra/imports/CartProduct.csv',
#         # Order: 'extra/imports/Order.csv',
#         # OrderProduct: 'extra/imports/OrderProduct.csv',
#         # Product: 'extra/imports/Product.csv',
#         # Shipping: 'extra/imports/Shipping.csv',
#         # User: 'extra/imports/User.csv',
#     }

#     def read_csv_file(csv_file):
#         with open(csv_file, 'r') as file:
#             reader = csv.DictReader(file)
#             data = [dict(row) for row in reader]
#         return data

#     def insert_data(table, data):
#         for row in data:
#             for key, value in row.items():
#                 if value == '':
#                     row[key] = None
#             obj = table(**row)
#             db.session.add(obj)
#         db.session.commit()

#     for table, csv_file in table_csv_mapping.items():
#         if db.session.query(table).first() is None:
#             data = read_csv_file(csv_file)
#             insert_data(table, data)
#         else:
#             print(f"Skipping import for table {table.__name__}. It is not empty.")


def import_csv_data(db):
    table_csv_mapping = {
        Master: 'imports/Master.csv'
        # Cart: 'extra/imports/Cart.csv',
        # CartProduct: 'extra/imports/CartProduct.csv',
        # Order: 'extra/imports/Order.csv',
        # OrderProduct: 'extra/imports/OrderProduct.csv',
        # Product: 'extra/imports/Product.csv',
        # Shipping: 'extra/imports/Shipping.csv',
        # User: 'extra/imports/User.csv',
    }

    def read_csv_file(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]
        return data

    def import_data_from_csv(table, csv_file):
        if db.session.query(table).first() is None:
            data = read_csv_file(csv_file)
            objects = [table(**row) for row in data]
            db.session.add_all(objects)
            db.session.commit()
        else:
            print(f"Skipping import for table {table.__name__}. It is not empty.")

    for table, csv_file in table_csv_mapping.items():
        import_data_from_csv(table, csv_file)

def export_csv_data(db):
    export_directory = 'exports/csv'
    os.makedirs(export_directory, exist_ok=True)

    for table_name, table in db.metadata.tables.items():
        csv_file = os.path.join(export_directory, f"{table_name}.csv")
        data = []
        columns = [column.name for column in table.columns]
        query = db.session.query(table).yield_per(1000)  # Adjust the batch size as per your needs
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in query:
                row_data = {column: getattr(row, column) for column in columns}
                writer.writerow(row_data)

                
def migrate_data(db):
    # Retrieve all records from the `master` table
    masters = Master.query.all()

    # Prepare the data for bulk inserts
    albums = []
    tracks = []
    playlists = []

    for master in masters:
        # Create a new album record
        album = Album(name=master.album, master_id=master.id)
        albums.append(album)

        # Create a new track record
        track = Track(name=master.title, url_ytm=master.track_url_ytm, master_id=master.id)
        tracks.append(track)

        # Create a new playlist record
        playlist = Playlist(name=master.pltst_name)
        playlists.append(playlist)

        # Associate the track with the playlist
        track.playlist = playlist

    # Add all the records to the session
    db.session.add_all(albums)
    db.session.add_all(tracks)
    db.session.add_all(playlists)

    # Commit the changes to the database
    db.session.commit()

            
