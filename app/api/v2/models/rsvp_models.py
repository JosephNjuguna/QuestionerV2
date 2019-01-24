"""
meetup database connection and  model 
"""
# inbuilt modules
import datetime
import psycopg2.extras
#import uuid
# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import BaseModel


class rsvp_model(BaseModel):
    def __init__(self, topic="", status="", username="", m_id=""):
        self.db = init_db()
        self.topic = topic
        self.status = status
        self.username = username
        self.rsvp_on = datetime.datetime.utcnow()
        self.m_id = m_id

    def check_meetup_exist(self, m_id, topic):
        """check whether the meetup exist or not"""
        curr = self.db.cursor()
        query = "SELECT id FROM meetup WHERE id = '%s'" % (m_id)
        curr.execute(query)
        if curr.fetchone() is not None:
            return True

    def check_user_name(self, username):
        """check if username exist"""
        curr = self.db.cursor()
        query = "SELECT username FROM users WHERE username = '%s'" % (username)
        curr.execute(query)
        if curr.fetchone() is not None:
            return True

    def check_user_rsvp(self, username):
        """check if username exist"""
        curr = self.db.cursor()
        query = "SELECT username FROM rsvp WHERE username = '%s'" % (username)
        curr.execute(query)
        if curr.fetchone() is not None:
            return True
            
    def rsvp_meetup(self):
        database = self.db
        cur = database.cursor()
        query = """INSERT INTO rsvp (rsvpdate, topic, userstatus, username) 
            VALUES ('{}', '{}', '{}', '{}') RETURNING id;
            """.format(self.rsvp_on, self.topic, self.status, self.username)
        cur.execute(query)
        rsvp_id = cur.fetchone()[0]
        database.commit()
        cur.close()
        return int(rsvp_id)
