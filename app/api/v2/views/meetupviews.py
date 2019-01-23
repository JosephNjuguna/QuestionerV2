import datetime
#downloaded dependencies
from flask_restful import Resource
from flask import request, make_response, jsonify
#local imports
from app.api.v2.models.meetup import MeetUp
from app.api.v2.utilis.validations import CheckData
args = ""
empty_loction ={"message":"Empty Meetup location"}
empty_topic ={"message":"Empty Meetup topic field"}
empty_date = {"message":"Empty date on when meetup is to happen"}
empty_tag = {"message":"Please enter a  Tag"}
empty_id = {"message":"please add your profile id"}

class PostMeetup(Resource):
    """admin create meetup endpoint"""
    def post(self):
        try:
            data = request.get_json()
            createdon = datetime.datetime.utcnow()
            location = data['location']
            topic = data['topic']
            happeningon = data['happeningon']
            tags = data['tag']
            user_state = data['isAdmin']

            """validate that all data is available"""
            if len(location) == 0:
                return empty_loction

            if len(topic) == 0:
                return empty_topic

            if len(happeningon) == 0:
                return empty_date

            if len(tags) == 0:
                return empty_tag
            
            if len(user_state) == 0:
                return empty_id

            meetupdata= {
                "createdon":createdon,
                "location":location,
                "topic": topic,
                "happeningon": happeningon,
                "tags":tags,
                'user_state': user_state
            }
            """pass meetup dict to Meetup Models"""
            meetup_db = MeetUp(**meetupdata)
            saved = meetup_db.create_meetup()
            resp = {
                "message": "Meetup Succesfully Created",
                "meetup": topic,
                "meetup_id": "{}".format(saved)
            }
            if saved == True:
                return make_response(jsonify({"message":"Meet already up exist"}),409)
            return resp,201
            meetup_db.close_db()

        except KeyError:
            return make_response(jsonify({"message":"Key Error"}),500)

class GetMeetup(Resource):
    def __init__(self):
        pass

class UpcomingMeetup(Resource):
    def __init__(self):
        pass

class SpecificMeetup(Resource):   
    def __init__(self):
        pass

class DeleteMeetUp(Resource):
    def __init__(self):
        pass

class UpdateMeetUp(Resource):
    def __init__(self):
        pass
