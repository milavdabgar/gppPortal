from app import create_app
from app.auth.forms import ExtendedRegisterForm

app, api = create_app()
app.config['SECURITY_REGISTER_USER_FORM'] = ExtendedRegisterForm 

if __name__ == "__main__":
    app.run(debug=True)