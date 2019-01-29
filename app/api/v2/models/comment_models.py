#inbuilt modules
import datetime
# local imports
from app.api.v2.models.basemodel import DatabaseConnection as connection
class CommentsModel(connection):
    """questions class"""
    def __init__(self, comment_body="question",meetup_id=0, question_id=0, user_id=0,):
        """class constructor"""
        self.comment_body = comment_body
        self.question_id = question_id
        self.meetup_id = meetup_id
        self.user_id = user_id
        self.postedon = datetime.datetime.utcnow().strftime("%a/%b/%Y")
    
    def check_meetup_id(self, m_id):
        """check whether the meetup exist or not"""
        query = """SELECT id FROM meetup WHERE id = '%s'""" % (m_id)
        result = self.fetch_single_data_row(query)
        if result is None:
            return False
        return True 

    def check_question_id(self, q_id):
        """check if question id exists"""
        query = "SELECT id FROM questions WHERE id = '%s'" % (q_id)
        result = self.fetch_single_data_row(query)
        if result is None:
            return False
        return False
    
    def check_comment_exist(self, question_body):
        """check if comment already exists"""
        query = "SELECT  body FROM comments WHERE body = '%s'" % (question_body)
        result = self.fetch_single_data_row(query)
        if result is not None:
            return True
        return False

    def post_comment_db(self):
        """Add comment details to the database"""
        if self.check_comment_exist(self.comment_body):
            return True
        query = """INSERT INTO comments (createdon, postedby, questionid, body)
            VALUES ('{}', '{}', '{}', '{}')RETURNING id;
            """.format(self.postedon, self.user_id, self.question_id, self.comment_body)
        result = self.save_incoming_data_or_updates(query)
        return result
    