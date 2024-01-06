from app import create_app
from app.api.users import UserResource

app, api = create_app()

api.add_resource(
    UserResource,
    "/user_list",
    "/users/<int:user_id>",
    "/users/add",
    "/users/edit/<int:user_id>",
    "/users/delete/<int:user_id>",
)

if __name__ == "__main__":
    app.run(debug=True)