"""questions view"""
#input modules
import datetime
#imports
from flask_restful import Resource
from flask import request, make_response, jsonify
#local import
from app.api.v2.utilis.validations import CheckData
from app.api.v2.models.questions import QuestionsModel
#error messages
empty_question_title = "Question title empty. Please input data"
empty_question_body = "Question body empty. Please input data"

class PostQuestion(Resource):
    """post question class"""
    def post(self, m_id):
        try:
            data = request.get_json()
            
            question_body = data['question_body']
            question_title = data['question_title']
            meetup_id = m_id
            user_id = 1
            votes = 0  

            question = {
                "question_body":question_body,
                "question_title":question_title,
                "meetup_id": meetup_id,
                "user_id":user_id,
                "votes":votes
            }
            if len(question_title)== 0:
                return make_response(jsonify({"message": empty_question_title}),400)

            if len(question_body)== 0:
                return make_response(jsonify({"message": empty_question_body }),400)
            
            question_data = QuestionsModel(**question)
            saved = question_data.post_question_db()
            question_id = saved
            resp = {
                "message": "Question successfully posted",
                "username": question_body,
                "user_id": "{}".format(question_id)
            }
            if saved == True:
                return make_response(jsonify({"Message":"Question already exist"}),409)
            return resp, 201
            question_data.close_db()

        except KeyError:
            return make_response(jsonify({"status":500, "message": "Internal server error"}),500)
      
class GetQuestionsMeetup(Resource):
    def __init__(self):
        pass

class GetSingleQuestion(Resource):
    """get single question class"""
    def __init__(self):
        pass

class UpvoteQuestion(Resource):
    """upvote question class"""
    def __init__(self):
        pass

class DownVoteQuestion(Resource):
    """downvote question class"""
    def __init__(self):
        pass
