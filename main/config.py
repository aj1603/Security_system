from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath('.'), '.env'))

class Config():
    FLASK_ENV = 'something'

    # Database configuration
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_ECHO = 0
    SQLALCHEMY_DATABASE_URI = "sqlite:///security.db"
    BABEL_DEFAULT_LOCALE = 'tk'