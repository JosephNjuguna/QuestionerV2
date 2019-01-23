"""
meetup database connection and  model 
"""
#inbuilt modules
import datetime
#import uuid
# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import BaseModel
#class
class MeetUp(BaseModel):
    def __init__(self, createdon="1/1/2018", location="unknown", topic="unknown", happeningon="1/1/2018", tags="unknown", user_id=0):
        """class constructor"""
        self.db = init_db()
        self.createdon = createdon
        self.location = location
        self.topic = topic
        self.happeningon = happeningon
        self.tags = tags
        self.user_id = user_id
    
    def check_meetup_exist(self, topic):
        """check whether the meetup exist or not"""
        curr = self.db.cursor()
        query = "SELECT topic FROM meetup WHERE topic = '%s'" % (topic)
        curr.execute(query)
        return curr.fetchone() is not None
    
    def check_user_admin(self, user_id):
        """check whether user id admin or not"""
        curr = self.db.cursor()
        query = "SELECT id FROM users WHERE id = '%s'" % (user_id)
        curr.execute(query)
        return curr.fetchone() is not None

    def create_meetup(self):
        meetup_data = {
            "topic": self.topic,
        }
        """check if user is admin"""
        if not self.check_user_admin(self.user_id):
            return "You dont have access"
        """check if question exist"""
        if self.check_meetup_exist(meetup_data['topic']):
            return "Meetup already exist"
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
