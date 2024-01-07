# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_security import Security
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_caching import Cache


# Initialize extensions, but without any specific app bound to them.
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
mail = Mail()
security = Security()
ma = Marshmallow()
cache = Cache()
