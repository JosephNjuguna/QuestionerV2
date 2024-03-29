"""
question database connection and  model 
"""
#inbuilt modules
import datetime
import uuid
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
        self.question_id = str(uuid.uuid4())
    
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
    
    def check_meetup_id(self, m_id):
        """check whether the meetup exist or not"""
        query = """SELECT id FROM meetup WHERE id = '%s'""" % (m_id)
        result = self.fetch_single_data_row(query)
        return result is not None

    def post_question_db(self):
        """Add question details to the database"""
        if self.check_question_exist(self.question_body):
            return True
        query = """INSERT INTO questions (createdon, postedby, meetupid, questionid, title, body, votes)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')RETURNING id;
            """.format(self.postedon, self.user_id, self.meetup_id, self.question_id, self.question_title, self.question_body, self.votes)
        result = self.save_incoming_data_or_updates(query)
        return result
    
    def get_questions(self , m_id):
        """get question from db"""
        query = "SELECT * FROM questions WHERE meetupid = '%s'" % (m_id)
        result = self.fetch_all_tables_rows(query)
        return result
        
    def get_specificquestion(self ,m_id, q_id):
        """get specific question from db"""
        query = """SELECT id, createdon, postedby, meetupid, title, body, votes FROM questions WHERE id = '%s' """ %(q_id)
        result = self.fetch_single_data_row(query)
        return result

    def upvote_question(self,m_id, q_id):
        query = "SELECT id, createdon, postedby, meetupid, title, body, votes FROM questions WHERE id = '%s'" % (q_id)
        data = self.fetch_single_data_row(query)
        return data
