import unittest
import os
import json
from app import create_app

class UsersTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing").test_client()
#test good sign up 201
        self.user1 = {
            "firstname": "Joseph",
            "lastname":"TheArtist",
            "email": "test1@mail.com",
            "password":"testpassword1",
            "confirm_password":"testpassword1",
            "phone":"075",
            "username":"Alan"
        }
#test valid log in 200
        self.user2 = {
            "email": 'test1@mail.com',
            "password": 'testpassword1'
        }
    """test sign up/sign in api endpoint"""
    def test_1_sign_up(self):
        """user good sign up (201)"""
        response = self.app.post('/api/v2/auth/signup', data=json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 201)