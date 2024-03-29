"""questions view"""
#input modules
import datetime
#imports
from flask_restful import Resource
from flask import request, make_response, jsonify
#local import
from app.api.v2.utilis.validations import CheckData
from app.api.v2.models.questions import QuestionsModel
from app.api.v2.models.meetup import MeetUp

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
                "question_id": "{}".format(question_id)
            }
            if saved == True:
                return make_response(jsonify({"Message":"Question already exist"}),409)
            return resp, 201

        except KeyError:
            return make_response(jsonify({"status":400, "message": "Missing either Question body or Question title input"}),400)    
class GetQuestionsMeetup(Resource):
    def get(self, m_id):
        questions = QuestionsModel()
        single_meetup_questions= questions.get_questions(m_id)
        meetup_exist = questions.check_meetup_id(m_id)
        if not meetup_exist:
            return make_response(jsonify({"message":"No Questions asked on this meetup or that Meetup doesnt exist"}))
        resp = {
            "status":200,
            "message":"all meetups",
            "data":[{
                "meetups": single_meetup_questions
                }]
        }
        return make_response(jsonify({"message": resp}),200)

class GetSingleQuestion(Resource):
    """get single question class"""
    def get(self, m_id, q_id ):
        single_question = QuestionsModel()
        one_meetup_questions= single_question.get_specificquestion(m_id, q_id)
        meetup_exist = single_question.check_meetup_id(m_id)
        if not meetup_exist:
            return make_response(jsonify({"message":"Meetup id doesnt exist"}))
        resp = {
            "status":200,
            "message":"all meetups",
            "data":[{
                "meetups":one_meetup_questions
                }]
        }
        return make_response(jsonify({"message": resp}),200)

class UpvoteQuestion(Resource):
    """upvote question class"""
    @staticmethod
    def patch(m_id, q_id):
        upvoted = QuestionsModel().upvote_question(m_id, q_id)
        question_id, question_createdon, question_title, question_body, question_votes= upvoted
        resp = {
            "id":question_id,
            "createdon": question_createdon,
            "question_meetup_id":question_body,
            "question_title":question_title,
            "question_body":question_body,
            "votes":question_votes
        }
        print(resp)

class DownVoteQuestion(Resource):
    """downvote question class"""
    def __init__(self):
        pass
