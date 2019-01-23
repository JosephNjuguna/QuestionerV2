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
    def __init__(self):
        self.data = request.get_json()
        self.createdon = datetime.datetime.utcnow()
        self.location = self.data['location']
        self.topic = self.data['topic']
        self.happeningon = self.data['happeningon']
        self.tags = self.data['tag']
        self.user_state = self.data['isAdmin']

    def post(self):
            """validate that all data is available"""
            if len(self.location) == 0:
                return make_response(jsonify(empty_loction),400)

            if len(self.topic) == 0:
                return empty_topic,400

            if len(self.happeningon) == 0:
                return empty_date,400

            if len(self.tags) == 0:
                return empty_tag,400
            
            if len(self.user_state) == 0:
                return empty_id,400

            meetupdata= {
                "createdon":self.createdon,
                "location":self.location,
                "topic": self.topic,
                "happeningon":self.happeningon,
                "tags":self.tags,
                'user_state': self.user_state
            }
            """pass meetup dict to Meetup Models"""
            meetup_db = MeetUp(**meetupdata)
            saved = meetup_db.create_meetup()
            resp = {
                "message": "Meetup Succesfully Created",
                "meetup": self.topic,
                "meetup_id": "{}".format(saved)
            }
            if saved == True:
                return make_response(jsonify({"message":"Meet already up exist"}),409)
            return resp,201
            meetup_db.close_db()

class GetMeetup(Resource):
    def get(self):
        meetups = MeetUp()
        all_meetups = meetups.get_meetups()
        resp = {
            "status":200,
            "message":"all meetups",
            "data":[{
                "meetups":str(all_meetups)
            }]
        }
        meetups.close_db()
        return resp,200
class UpcomingMeetup(Resource):
    def __init__(self):
        pass
class SpecificMeetup(Resource):   
    def get(self, m_id):
        """get a specific meetup"""
        one_meetup = MeetUp()
        single_meetup_data =one_meetup.get_specific_meetup(m_id)
        if single_meetup_data == False:
            return make_response(jsonify({"message":"Meetup not found"}),404)
        return make_response(jsonify({
                "status":200,
                "message":"Meetup found",
                "data":[{
                    "meetup": single_meetup_data
                }]}),200)

class DeleteMeetUp(Resource):
    def __init__(self):
        pass

class UpdateMeetUp(Resource):
    def __init__(self):
        pass
