"""test for api endpoints"""
# inbuilt modules
import json
import unittest
# local imports
from app import create_app
class MeetupTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app.test_client()
        self.record1 = {
            "location":"Kenya ,Safaricom",
            "topic":"Da",
            "happeningon":"1/1/2018",
            "tag":"@comeall"
        }
    """test api endpoints"""
    def test_admin_create_meetup(self):
        """test that admin post question successfully (201)"""
        response = self.app.post('/api/v2/meetup', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
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
        response = self.app.get('/api/v2/meetup/1', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_delete_a_meetup(self):
        """user should be able to get a specific meetup"""
        response = self.app.delete('/api/v2/meetup/1', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_update_a_meetup(self):
        """user should be able to get a specific meetup"""
        response = self.app.put('/api/v2/meetup/1', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    