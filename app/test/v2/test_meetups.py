import unittest
import os
import pytest
from app import create_app

class UsersTest(unittest.TestCase):
    def setUp(self):
        self.application = create_app
        self.app = self.application.test_client()

    """test api endpoints"""
    def test_1_admin_create_meetup(self):
        """test that admin post question successfully (201)"""
        pass
    
    def test_2_get_upcoming_meetup(self):
        """test that a meetup exist already (409 conflict error)"""
        pass
    def test_3_get_specific_meetup(self):
        """user should be able to get a specific meetup"""
        pass

    """test validations"""
    def test_meetup_id_exist(self):
        """test user tries to enter same meetup (409 conflict)"""
        pass
    
    def test_fetch_nonexistance_id(self):
        """test when user tries to fetch unavailable meetup id"""
        pass

    def test_invalid_key_entry(self):
        """test that input data there is an empty key (400 empty key)"""
        pass

    def test_empty_value_entry(self):
        """test if admin tries to insert a dictkey which is empty (400)"""