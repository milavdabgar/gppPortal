import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.dirname(basedir)
load_dotenv(os.path.join(parentdir, ".env"))

class Config:
    DEBUG = True
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    
class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(parentdir, "instance")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    #     SQLITE_DB_DIR, "GPPPortal.sqlite"
    # )
    SQLALCHEMY_DATABASE_URI = "sqlite:///GPPPortal.sqlite"
    DEBUG = True