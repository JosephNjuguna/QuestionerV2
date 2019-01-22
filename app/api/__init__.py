from flask_restful import Api
from flask import Blueprint
#local imports

from app.api.v2.views.userviews import (SignUp, LogIn, UserResetPassword, OneUser, UserUpdateInfo)
from app.api.v2.views.meetupviews import (PostMeetup, GetMeetup ,UpcomingMeetup,SpecificMeetup,DeleteMeetUp,UpdateMeetUp)
from app.api.v2.views.questionsviews import (PostQuestion,GetQuestionsMeetup, GetSingleQuestion, UpvoteQuestion, DownVoteQuestion)
version_two = Blueprint('version_two',__name__)
api = Api(version_two)
#user authentication
api.add_resource(SignUp, '/auth/signup')
api.add_resource(LogIn,'/auth/login')
api.add_resource(OneUser, '/users/<int:user_id>')
#-------------------------------------------------------------
api.add_resource(UserUpdateInfo, '/users/<int:user_id>/update')
api.add_resource(UserResetPassword, '/auth/passwordreset')
#meetup
api.add_resource(PostMeetup, '/meetup')
api.add_resource(GetMeetup, '/meetup')
api.add_resource(UpcomingMeetup, '/meetup/upcoming')
api.add_resource(SpecificMeetup, '/meetup/upcoming/<int:m_id>')
#--------------------------------------------------------
api.add_resource(DeleteMeetUp, '/meetup/<int:m_id>/delete')
api.add_resource(UpdateMeetUp, '/meetup/<int:m_id>/update')
#questions
api.add_resource(PostQuestion , '/meetup/<int:m_id>/question')
api.add_resource(GetQuestionsMeetup , '/meetup/<int:m_id>/question')
api.add_resource(GetSingleQuestion, '/meetup/<int:m_id>/question/<int:q_id>')
api.add_resource(UpvoteQuestion, '/meetup/<int:m_id>/question/<int:q_id>/upvote')
api.add_resource(DownVoteQuestion, '/meetup/<int:m_id>/question/<int:q_id>/downvote')