import unittest
import os
import pytest
from app import create_app

class UsersTest(unittest.TestCase):
    def setUp(self):
        self.application = create_app
        self.app = self.application.test_client()

    """test sign up/sign in api endpoint"""
    def test_2_user_sign_up(self):
        """user good sign up (201)"""
        pass
    
    def test_3_user_sign_in(self):
        """user good login (200)"""
        pass 

    def test_4_get_specific_user(self):
        """user should be able to view and access their profile (200)"""
        pass
    
    """testing  validations"""
    def test_1_user_exist(self):
        """test if user already exist (409)"""
        pass

    def test_4_user_missing_key(self):
        """user input missing a data in a value (400)"""
        pass

    def test_5_user_missing_value(self):
        """test a user has no key in his/her input (400)"""
        pass 

    def test_6_username_too_short(self):
        """username is less than 3 (400)"""
        pass

    def test_7_valid_email(self):
        """test that user has entered an invalid email address (400)"""
        pass

    def test_8_user_password_mismatch(self):
        """test that password and confirm password mis-match(400)"""
        pass