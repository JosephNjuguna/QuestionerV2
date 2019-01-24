"""
meetup database connection and  model 
"""
# inbuilt modules
import datetime
import psycopg2.extras
#import uuid
# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import DatabaseConnection as connection


class rsvp_model(connection):
    def __init__(self, topic="", status="", username="", m_id=""):
        self.topic = topic
        self.status = status
        self.username = username
        self.rsvp_on = datetime.datetime.utcnow()
        self.m_id = m_id

    def check_meetup_exist(self, m_id, topic):
        """check whether the meetup exist or not"""
        query = "SELECT id FROM meetup WHERE id = '%s'" % (m_id)
        result = self.fetch_single_data_row(query)
        return result

    def check_user_name(self, username):
        """check if username exist"""
        query = "SELECT username FROM users WHERE username = '%s'" % (username)
        result = self.fetch_single_data_row(query)
        return result

    def check_user_rsvp(self, username):
        """check if username exist"""
        query = "SELECT username FROM rsvp WHERE username = '%s'" % (username)
        result = self.fetch_single_data_row(query)
        return result
    
    def rsvp_meetup(self):
        if self.check_user_rsvp(self.username):
            return True
        query = """INSERT INTO rsvp (rsvpdate, topic, userstatus, username) 
            VALUES ('{}', '{}', '{}', '{}') RETURNING id;
            """.format(self.rsvp_on, self.topic, self.status, self.username)
        result = self.save_incoming_data_or_updates(query)
        return result
