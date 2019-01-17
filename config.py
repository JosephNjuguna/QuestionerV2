"""configuring application"""
import os
#local imports
from instance.config import SECRET_KEY,DB_CONNECTION

from config import SECRET_KEY,DB_CONNECTION

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = SECRET_KEY
    DATABASE_URL = DB_CONNECTION

class DevelopmentConfig(Config):
    """Development phase configurations"""
    DEBUG = True

class TestingConfig(Config):
    """Testing Configurations."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = DB_CONNECTION

class ReleaseConfig(Config):
    """Release Configurations."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}