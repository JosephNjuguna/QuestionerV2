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

class Meetup(Resource):
    """admin create meetup endpoint"""
    def post(self):
        #try:
            data = request.get_json()
            createdon = datetime.datetime.utcnow().strftime("%a/%b/%Y")
            location = data['location']
            topic = data['topic']
            happeningon = data['happeningon']
            tags = data['tag']
        
            """validate that all data is available"""
            if len(location) == 0:
                return make_response(jsonify(empty_loction),400)

            if len(topic) == 0:
                return empty_topic,400

            if len(happeningon) == 0:
                return empty_date,400

            if len(tags) == 0:
                return empty_tag,400

            meetupdata= {
                "created_on":createdon,
                "location":location,
                "topic": topic,
                "happening_on":happeningon,
                "tags":tags,
            }
            """pass meetup dict to Meetup Models"""
            meetup_db = MeetUp(**meetupdata)
            saved = meetup_db.create_meetup()
            resp = {
                "message": "Meetup Succesfully Created",
                "meetup": topic,
                "created_on":createdon,
                "meetup_id":saved
            }
            if saved == True:
                return make_response(jsonify({"message":"Meetup already up exist"}),409)
            return resp,201
        #except:
            #return make_response(jsonify({"message":"Please check your keys. Either Meetup: topic,location,tags"}),400)
    
    @staticmethod
    def get():
        meetups = MeetUp()
        meet_up = meetups.get_meetups()
        resp = {
            "status":200,
            "message":"all meetups",
            "data":[{"meetups":meet_up}]
        }
        return resp,200
    
    def delete(self,m_id):
        """delete a specific meetup"""
        one_meetup = MeetUp()
        delete_meetup_data = one_meetup.delete_specific_meetup(m_id)
        resp = {
            "status":200,
            "message":"Meetup Deleted",
            "data":[{
                "meetup": delete_meetup_data
            }]
        }
        if delete_meetup_data == True:
            return make_response(jsonify({"message": resp}),200)
        return make_response(jsonify({"message":"Meetup not found"}),404)
class SpecificUpcomingMeetup(Resource):   
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

