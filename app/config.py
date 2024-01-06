import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.dirname(basedir)
load_dotenv(os.path.join(parentdir, ".env"))


class Config:
    DEBUG = False
    TESTING = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'admin@email.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "password"
    # ADMINS = ['milav.dabgar@gmail.com']
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')


    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH") or "bcrypt"
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT") or "super secret"
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_TOKEN_AUTHENTICATION_HEADER = None
    WTF_CSRF_ENABLED = False



class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///GPPPortal.sqlite"
    # CACHE_TYPE = "RedisCache"
    # CACHE_REDIS_HOST = "localhost"
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_DB = 3
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    # SECURITY_CONFIRMABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_CHANGEABLE = True
    # SECURITY_REGISTER_USER_FORM = "ExtendedRegisterForm"
    # SECURITY_LOGIN_FORM = "ExtendedLoginForm"
    # SECURITY_URL_PREFIX = '/auth'
    # SECURITY_EMAIL_RESET_PASSWORD_TEMPLATE = 'auth/reset_password_instructions.html'
    
