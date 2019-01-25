"""questions view"""
#input modules
import datetime
#imports
from flask_restful import Resource
from flask import request, make_response, jsonify
#local import
from app.api.v2.utilis.validations import CheckData
from app.api.v2.models.comment_models import CommentsModel
from app.api.v2.models.meetup import MeetUp

#error messages
empty_question_body = "Comment body empty. Please input data"

class postComment(Resource):
    """post question class"""
    def post(self, m_id, q_id):
        try:
            data = request.get_json()
            
            comment_body = data['comment_body']
            meetup_id = m_id
            question_id = q_id
            user_id = 1

            comment = {
                "comment_body":comment_body,
                "meetup_id":m_id,
                "question_id": question_id,
                "user_id":user_id,
            }
            if len(comment_body)== 0:
                return make_response(jsonify({"message": empty_question_body }),400)
            
            comment_data = CommentsModel(**comment)
            saved = comment_data.post_comment_db()
            question_id = saved
            resp = {
                "message": "Comment successfully posted",
                "body": comment_body,
                "comment_id": "{}".format(question_id)
            }
            if saved == True:
                return make_response(jsonify({"Message":"Comment already exist"}),409)
            return resp, 201

        except KeyError:
            return make_response(jsonify({"status":400, "message": "Missing Comment body"}),400)
