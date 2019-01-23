import datetime
#downloaded dependencies
from flask_restful import Resource
from flask import request, make_response, jsonify
#local imports
from app.api.v2.models.meetup import MeetUp
from app.api.v2.utilis.validations import CheckData
args = ""
class PostMeetup(Resource):
    """admin create meetup endpoint"""
    #@tokenrequired
    def post(self):
        try:
            data = request.get_json()
            createdon = datetime.datetime.utcnow()
            location = data['location']
            topic = data['topic']
            happeningon = data['happeningon']
            tags = data['tag']
            user_id = data['id']

            """validate that no key is empty"""
            CheckData.checkkey(data)

            meetupdata= {
                "createdon":createdon,
                "location":location,
                "topic": topic,
                "happeningon": happeningon,
                "tags":tags,
                'user_id': user_id
            }
            """pass meetup dict to Meetup Models"""
            meetup_db = MeetUp(**meetupdata)
            saved = meetup_db.create_meetup()
            meetup_id = saved
            resp = {
                "message": "Meetup Succesfully Created",
                "meetup": topic,
                "meetup_id": "{}".format(meetup_id)
            }
            meetup_db.close_db()
            return resp,201
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
