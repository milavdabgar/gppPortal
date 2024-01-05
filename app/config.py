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
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SECURITY_PASSWORD_SALT = (
        os.environ.get("SECURITY_PASSWORD_SALT") or "you-will-never-guess"
    )


class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(basedir, "instance")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    #     SQLITE_DB_DIR, "GPPPortal.sqlite"
    # )
    SQLALCHEMY_DATABASE_URI = "sqlite:///GPPPortal.sqlite"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    # CACHE_TYPE = "RedisCache"
    # CACHE_REDIS_HOST = "localhost"
    # CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_DB = 3
