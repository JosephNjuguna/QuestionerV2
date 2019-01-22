import unittest
import os
from app import create_app

class RsvpTest(unittest.TestCase):
    def setUp(self):
        self.application = create_app
        self.app = self.application.test_client()

    """test user rsvp api endpoint"""
    def test_1_user_rsvp(self):
        """test user rsvp successfuly (201)"""
        pass

    """test user rsvp validations"""
    def test_2_rsvp_exist(self):
        """test when user tries to rsvp twice (409)"""
        pass

    def test_3_invalid_meetup_id(self):
        """test that meetup id for rsvp (400)"""
        pass

    def test_4_empty_key(self):
        """test user has empty key (400)"""
        pass
        
    def test_3_empty_value(self):
        """test user input empty key (400)"""
        pass