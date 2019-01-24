"""
question database connection and  model 
"""
#inbuilt modules
import datetime
#import uuid
# local imports
from app.api.v2.models.basemodel import DatabaseConnection as connection
#class
class QuestionsModel(connection):
    """questions class"""
    def __init__(self, question_body="question", question_title="title", meetup_id=0, user_id=0, votes=0):
        """class constructor"""
        #from BaseModel module
        self.question_body = question_body
        self.question_title = question_title
        self.meetup_id = meetup_id
        self.user_id = user_id
        self.votes=votes
        self.postedon = datetime.datetime.utcnow()
    
    def check_question_exist(self, question_body):
        """check if question already exists"""
        query = "SELECT  body FROM questions WHERE body = '%s'" % (question_body)
        result = self.fetch_single_data_row(query)
        return result

    def check_question_id(self, q_id):
        """check if question id exists"""
        query = "SELECT id FROM questions WHERE id = '%s'" % (q_id)
        result = self.fetch_single_data_row(query)
        return result

    def post_question_db(self):
        """Add question details to the database"""
        if self.check_question_exist(self.question_body):
            return True
        query = """INSERT INTO questions (createdon, postedby, meetupid, title, body, votes)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}')RETURNING id;
            """.format(self.postedon, self.user_id, self.meetup_id, self.question_title, self.question_body, self.votes)
        result = self.save_incoming_data_or_updates(query)
        return result
    
    #remaining
    def upvote_question(self,m_id, q_id):
        if self.check_question_exist(q_id):
            return True
        query = "SELECT id, createdon, postedby, meetupid, title, body, votes FROM questions WHERE id = '%s'" % (q_id)
        data = self.fetch_single_data_row(query)
        return data
