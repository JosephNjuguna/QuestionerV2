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
#test password and passwordconfirm not matching 400
        self.user4 = {
            "firstname": "Joseph",
            "lastname": 'alan',
            "email": 'test1@mail.com',
            "password": 'a12njJOSE',
            "confirm_password": 'a12nj'  
        }
#test that email not found 404
        self.user5 = {
            "email": "test10mail.com",
            "password": "a12njose"
        }
#test incorrect password 400 in log in
        self.user6 = {
            "email": 'test1@mail.com',
            "password": 'a12nse'
        }
#test username too short
        self.user7 = {
            "firstname": "Jos",
            "lastname":"TheArtist",
            "email": "test1@mail.com",
            "password":"testpassword1",
            "confirm_password":"testpassword1",
            "phone":"075",
            "username":"Alan"
        }

    """test sign up/sign in api endpoint"""
    def test_1_user_sign_up(self):
        """user good sign up (201)"""
        response = self.app.post('/api/v2/auth/signup', data=json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_2_user_login(self):
        """user good log in  (200)"""
        response = self.app.post('/api/v2/auth/login', data=json.dumps(self.user2), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_user(self):
        """user should be able to view and access their profile (200)"""
        response = self.app.get('/api/v2/users/1', data=json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_user_info(self):
        """user can update their data"""
        response = self.app.get('/api/v2/users/1/update', data=json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 200)
