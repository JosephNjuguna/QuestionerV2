import datetime
#downloaded dependencies
from flask_restful import Resource
from flask import request, make_response, jsonify
#local imports
from app.api.v2.models.rsvp_models import rsvp_model
from app.api.v2.utilis.validations import CheckData

class rsvp_meetup(Resource):
    def post(self, m_id):
        try:
            data = request.get_json()
            topic = data['topic']
            status = data['status']
            username = data['username']

            if data['topic'] == "":
                return make_response(jsonify({"message": "Please Input data on your topic field" % ()}), 400)
            if data['status'] == "":
                return make_response(jsonify({"message": "Please Input Yes to rsvp and No to reject rsvp"}), 400)
            if data['username'] == "":
                return make_response(jsonify({"message": "Username can`t be empty. Input username"}), 400)
            rsvp_data = {
                "topic": topic,
                "status": status,
                "username":username,
                "m_id":m_id
            }
            rsvp_db = rsvp_model(**rsvp_data)
            rsvp_saved = rsvp_db.rsvp_meetup()

            check_meetup = rsvp_db.check_meetup_exist(m_id, topic)
            check_user = rsvp_db.check_user_name(username)
            check_user_rsvpd = rsvp_db.check_user_name(username)
            print(check_meetup)
            print(check_user)
            print(check_user_rsvpd)
            response= {
                "status": 201,
                "message": "Successfully rsvp for the %s meetup" %(topic),
                "user data": {
                    "rsvp_id" :"{}".format(rsvp_saved),
                    "data": rsvp_data
                }
            }, 201
            if check_meetup != True :
                return make_response(jsonify({"message":"Meetup id and topic not found"}),404)
            if check_user != True:
                return make_response(jsonify({"message":"Username not found"}),404)
            if check_user_rsvpd == True:
                return response
            return make_response(jsonify({"message":"You have RSVP for this Meetup"}),409)
            rsvp_db.close_db()

        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a topic, status, username field"}), 500)

