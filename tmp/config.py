import os

class Config:
    """Flask configuration variables."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = bool(os.getenv('DEBUG', False))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/brewery_management_system')
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False))
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH', 'cerulean')

class TestConfig(Config):
    """Flask test configuration variables."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
