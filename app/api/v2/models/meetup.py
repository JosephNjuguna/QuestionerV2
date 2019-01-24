"""
meetup database connection and  model 
"""
#inbuilt modules
import datetime
import psycopg2.extras
# local imports
from app.api.v2.models.basemodel import DatabaseConnection as connection
#class
class MeetUp(connection):
    def __init__(self, createdon="1/1/2018", location="unknown", topic="unknown", happeningon="1/1/2018", tags="unknown"):
        """class constructor"""
        self.createdon = createdon
        self.location = location
        self.topic = topic
        self.happeningon = happeningon
        self.tags = tags
    
    def check_meetup_exist(self, topic):
        """check whether the meetup exist or not"""
        query = """SELECT topic FROM meetup WHERE topic = '%s'""" % (topic)
        result = self.fetch_single_data_row(query)
        return result
    
    def check_meetup_id(self, m_id):
        """check whether the meetup exist or not"""
        query = """SELECT id FROM meetup WHERE id = '%s'""" % (m_id)
        result = self.fetch_single_data_row(query)
        return result
    
    def check_user_admin(self, user_state = "false"):
        """check whether user is admin or not"""
        query = "SELECT isAdmin FROM users WHERE isAdmin = '%s'" % (user_state)
        result = self.fetch_single_data_row(query)
        return result

    def create_meetup(self):
        meetup_data = {
            "topic": self.topic,
        }
        """check if question exist"""
        if self.check_meetup_exist(meetup_data['topic']):
            return True
        query = """INSERT INTO meetup (createdon, venue, topic, happening, tags) 
            VALUES ('{}', '{}', '{}', '{}', '{}') RETURNING id;
            """.format(self.createdon, self.location, self.topic, self.happeningon, self.tags)
        result = self.save_incoming_data_or_updates(query)
        return result

    def get_meetups(self):
        """get all meetup"""
        query = """SELECT id, createdon, venue, topic, happening, tags  FROM meetup"""
        result = self.fetch_all_tables_rows(query)
        return result

    def get_specific_meetup(self, m_id):
        """check meetup id exist"""
        if not self.check_meetup_id(m_id):
            return False
        """return a specific meetup available"""
        query = """SELECT id , createdon, venue, topic, happening, tags FROM meetup WHERE id = '%s' % (m_id)"""
        result = self.fetch_single_data_row(query)
        return result