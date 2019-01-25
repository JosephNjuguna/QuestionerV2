from flask_restful import Api
from flask import Blueprint
#local imports
from app.api.v2.views.rsvpviews import (rsvp_meetup)
from app.api.v2.views.commentview import (postComment)
from app.api.v2.views.meetupviews import (Meetup, SpecificUpcomingMeetup)
from app.api.v2.views.userviews import (SignUp, LogIn)
from app.api.v2.views.meetupviews import (Meetup, SpecificUpcomingMeetup)
from app.api.v2.views.questionsviews import (PostQuestion,GetQuestionsMeetup, GetSingleQuestion, UpvoteQuestion, DownVoteQuestion)
version_two = Blueprint('version_two',__name__)
api = Api(version_two)
api.add_resource(SignUp, '/auth/signup')
api.add_resource(LogIn,'/auth/login')
api.add_resource(Meetup, '/meetup', '/meetup/upcoming', '/meetup/upcoming/<int:m_id>/delete')
api.add_resource(SpecificUpcomingMeetup, '/meetup/upcoming/<int:m_id>')
api.add_resource(rsvp_meetup, '/meetup/upcoming/<int:m_id>/rsvp')
api.add_resource(postComment, '/meetup/<int:m_id>/question/<int:q_id>/comment')
api.add_resource(PostQuestion , '/meetup/<int:m_id>/question')
api.add_resource(GetQuestionsMeetup , '/meetup/<int:m_id>/question')
api.add_resource(GetSingleQuestion, '/meetup/<int:m_id>/question/<int:q_id>')
api.add_resource(UpvoteQuestion, '/meetup/<int:m_id>/question/<int:q_id>/upvote')
api.add_resource(DownVoteQuestion, '/meetup/<int:m_id>/question/<int:q_id>/downvote')