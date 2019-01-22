import os
import datetime

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)

class DevelopmentConfig(Config):
    """Development phase configurations"""
    DEBUG = True

class TestingConfig(Config):
    """Testing Configurations."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


class ReleaseConfig(Config):
    """Release Configurations."""
    DEBUG = False
    TESTING = False


app_config = {
    'config':Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}