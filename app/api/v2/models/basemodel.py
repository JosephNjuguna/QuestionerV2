"""
This module defines the base model
"""
import os
import datetime

from app.api.v2.models.database import init_db

class BaseModel(object):
    """
    This class encapsulates the functions of the base model
    that will be shared across all other models
    """
    def __init__(self):
        """initialize the database"""
        self.db = init_db()

    def close_db(self):
        """This function closes the database"""
        self.db.close()
        pass
    