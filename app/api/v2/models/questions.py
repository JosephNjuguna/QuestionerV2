"""
question database connection and  model 
"""
#inbuilt modules
import datetime
#import uuid
# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import BaseModel
#class
class QuestionsModel(BaseModel):
    """questions class"""
    def __init__(self, question_body="question", question_title="title", meetup_id=0, user_id=0, votes=0):
        """class constructor"""
        #from BaseModel module
        self.db = init_db()
        self.question_body = question_body
        self.question_title = question_title
        self.meetup_id = meetup_id
        self.user_id = user_id
        self.votes=votes
        self.postedon = datetime.datetime.utcnow()
    
    def check_question_exist(self, question_body):
        """check if question already exists"""
        curr = self.db.cursor()
        query = "SELECT  body FROM questions WHERE body = '%s'" % (question_body)
        curr.execute(query)
        return curr.fetchone() is not None

    def post_question_db(self):
        """Add question details to the database"""
        if self.check_question_exist(self.question_body):
            return True
        database = self.db
        curr = database.cursor()
        query = """INSERT INTO questions (createdon, postedby, meetupid, title, body, votes)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}')RETURNING id;
            """.format(self.postedon, self.user_id, self.meetup_id, self.question_title, self.question_body, self.votes)
        curr.execute(query)
        question_id = curr.fetchone()[0]
        database.commit()
        curr.close()
        return int(question_id)