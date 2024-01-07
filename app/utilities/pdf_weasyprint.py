from jinja2 import Template
from weasyprint import HTML
import uuid


def format_report(template_file, data={}):
    with open(template_file) as file_:
        template = Template(file_.read())
        return template.render(data=data)

def create_pdf_report(data):
    message = format_report("report-template.html", data=data)
    html = HTML(string=message)
    file_name = str(uuid.uuid4()) + ".pdf"
    print(file_name)
    html.write_pdf(target=file_name) 


def main():
    new_users = [
        {"name": "Raj", "email": "raj@example.com", "marks":{}},
        {"name": "Yasmin", "email": "yasmin@example.com", "marks":{}},
    ]
    for user in new_users:
        create_pdf_report(user)


if __name__ == "__main__":
    main()
