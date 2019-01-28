"""test for api endpoints"""
# inbuilt modules
import json
import unittest
# local imports
from app import create_app
class MeetupTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing").test_client()
        self.record1 = {
            "location":"Kenya ,Safaricom",
            "topic":"CNN MONEY",
            "happeningon":"1/1/2018",
            "tag":"@comeall",
            "isAdmin":"true"
        }
        self.record2 = {
            "location":"Kenya ,Safaricom",
            "topic":"Youtube ads",
            "happeningon":"1/1/2018",
            "tag":"@comeall",
            "isAdmin":"true"
        }
        self.record3 = {
            "location":"Kenya ,Safaricom",
            "topic":"",
            "happeningon":"1/1/2018",
            "tag":"@comeall",
            "isAdmin":"true"
        }
    """test api endpoints"""
    def test_meetup_posted_exist(self):
        """test that meetup exist"""
        response = self.app.post('/api/v2/meetup', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code,409)

    def test_get_meetup(self):
        """get meetup exist"""
        response = self.app.get('/api/v2/meetup', data=json.dumps(self.record2), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_empty_topic_meetup(self):
        """test that admin post question successfully (201)"""
        response = self.app.post('/api/v2/meetup', data=json.dumps(self.record3), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_all_meetup(self):
        """user should be able to get a specific meetup"""
        response = self.app.get('/api/v2/meetup', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_get_upcoming_meetup(self):
        """user should be able to get a specific meetup"""
        response = self.app.get('/api/v2/meetup/upcoming', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_meetup(self):
        """user should be able to get a specific meetup"""
        response = self.app.get('/api/v2/meetup/upcoming/1', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)