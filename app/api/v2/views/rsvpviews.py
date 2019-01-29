import datetime
#downloaded dependencies
from flask_restful import Resource
from flask import request, make_response, jsonify
#local imports
from app.api.v2.models.rsvp_models import rsvp_model
from app.api.v2.utilis.validations import CheckData
class rsvp_meetup(Resource):
    #@current_user
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
            if data['status'] == "Yes":
                rsvp_data = {
                    "topic": topic,
                    "status": status,
                    "username": username,
                    "m_id": m_id
                }
                rsvp_db = rsvp_model(**rsvp_data)
                rsvp_saved = rsvp_db.rsvp_meetup()
                response = {
                    "status": 201,
                    "message": "Successfully rsvp for the %s meetup" % (topic),
                    "user data": {
                        "rsvp_id": "{}".format(rsvp_saved),
                        "data": rsvp_data
                    }
                }, 201
                #check if meetup exist
                check_meetup = rsvp_db.check_meetup_exist(m_id)
                if check_meetup == False:
                    return make_response(jsonify({"message":"Meetup Id not found"}),404)
                
                #check if user exist
                check_user = rsvp_db.check_user_name(username)
                if check_user == False:
                    return make_response(jsonify({"message":"User not found"}),404)
                user_rsvp_already = rsvp_db.check_user_rsvp(username)
                if user_rsvp_already == True:
                    return make_response(jsonify({"message":"You already have RSVP for this meetup"}))
                return make_response(jsonify({"message": response}),201)
            if data['status'] == 'No':
                return make_response(jsonify({"message":"Thank you.You can still rsvp before Meetup deadline"})) 
            if data['status'] != 'No' or  data['status'] != 'Yes':
                return make_response(jsonify({"message":"Please enter a valid RSVP response. Either a YES or NO"})) 
        
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a topic, status, username field"}), 500)
