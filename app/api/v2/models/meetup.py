"""
meetup database connection and  model 
"""
#inbuilt modules
import datetime
import psycopg2.extras
#import uuid
# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import BaseModel
#class
class MeetUp(BaseModel):
    def __init__(self, createdon="1/1/2018", location="unknown", topic="unknown", happeningon="1/1/2018", tags="unknown", user_state=""):
        """class constructor"""
        self.db = init_db()
        self.createdon = createdon
        self.location = location
        self.topic = topic
        self.happeningon = happeningon
        self.tags = tags
        self.user_state = user_state
    
    def check_meetup_exist(self, topic):
        """check whether the meetup exist or not"""
        curr = self.db.cursor()
        query = "SELECT topic FROM meetup WHERE topic = '%s'" % (topic)
        curr.execute(query)
        return curr.fetchone() is not None
    
    def check_meetup_id(self, m_id):
        """check whether the meetup exist or not"""
        curr = self.db.cursor()
        query = "SELECT id FROM meetup WHERE id = '%s'" % (m_id)
        curr.execute(query)
        return curr.fetchone() is not None
    
    def check_user_admin(self, user_state = "false"):
        """check whether user is admin or not"""
        curr = self.db.cursor()
        query = "SELECT isAdmin FROM users WHERE isAdmin = '%s'" % (user_state)
        curr.execute(query)
        return curr.fetchone() is not None

    def create_meetup(self):
        meetup_data = {
            "topic": self.topic,
        }
        """check if question exist"""
        if self.check_meetup_exist(meetup_data['topic']):
            return True
        database = self.db
        cur = database.cursor()
        query = """INSERT INTO meetup (createdon, venue, topic, happening, tags) 
            VALUES ('{}', '{}', '{}', '{}', '{}') RETURNING id;
            """.format(self.createdon, self.location, self.topic, self.happeningon, self.tags)
        cur.execute(query)
        print("inserted")
        meetup_id = cur.fetchone()[0]
        database.commit()
        cur.close()
        return int(meetup_id)

    def get_meetups(self):
        """get all meetup"""
        curr = self.db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "SELECT id, createdon, venue, topic, happening, tags  FROM meetup"
        curr.execute(query)
        data = curr.fetchall()
        curr.close()
        return data

    def get_specific_meetup(self, m_id):
        """check meetup id exist"""
        if not self.check_meetup_id(m_id):
            return False
        """return a specific meetup available"""
        curr = self.db.cursor()
        query = "SELECT id , createdon, venue, topic, happening, tags FROM meetup WHERE id = '%s'" % (m_id)
        curr.execute(query)
        return curr.fetchone()