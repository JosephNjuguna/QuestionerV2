"""testing questions url api endpoints """
import json
import unittest
# local imports
from app import create_app

class QuestionsTest(unittest.TestCase):
    """Testing Question URL API endpoints"""
    def setUp(self):
        self.application = create_app
        self.app = self.application.test_client()
        
        self.question1 = {
            "question_body":"Youtube ads are everything??",
            "question_title":"Youtube"
        }

        self.question2 = {
            "question_body":"Youtube ads are everything",
            "question_title":""
        }

        self.question3 = {
            "question_body":"",
            "question_title":"Youtube"
        }

    def test_qood_question_post(self):
        """test that user post a question with all required fields"""
        response = self.app.post('/api/v2/meetup/1/question', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_questions(self):
        """test that user post a question with all required fields"""
        response = self.app.get('/api/v2/meetup/1/question', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_single_questions(self):
        """test that user post a question with all required fields"""
        response = self.app.get('/api/v2/meetup/1/question/1', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_upvote_questions(self):
        """test that user post a question with all required fields"""
        response = self.app.patch('/api/v2/meetup/1/question/1/upvote', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 204)
    
    def test_downvote_questions(self):
        """test that user post a question with all required fields"""
        response = self.app.patch('/api/v2/meetup/1/question/1/downvote', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_empty_title_question_post(self):
        """test user input question with empty title"""
        response = self.app.post('/api/v2/meetup/1/question', data=json.dumps(self.question2), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_empty_body_question_post(self):
        """test user inputs"""
        response = self.app.post('/api/v2/meetup/1/question', data=json.dumps(self.question3), content_type='application/json')
        self.assertEqual(response.status_code, 400)
