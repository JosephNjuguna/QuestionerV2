"""questions view"""
from flask_restful import Resource

class PostQuestion(Resource):
    """post question class"""
    def __init__(self):
        pass
      
class GetQuestionsMeetup(Resource):
    def __init__(self):
        pass

class GetSingleQuestion(Resource):
    """get single question class"""
    def __init__(self):
        pass

class UpvoteQuestion(Resource):
    """upvote question class"""
    def __init__(self):
        pass

class DownVoteQuestion(Resource):
    """downvote question class"""
    def __init__(self):
        pass
