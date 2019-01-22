import unittest
import os
import pytest
from app import create_app

class UsersTest(unittest.TestCase):
    def setUp(self):
        self.application = create_app
        self.app = self.application.test_client()

    """test api endpoints"""
    def test_1_question_post(self):
        """test user post question successfully (201)"""
        pass
    
    def test_2_get_questions(self):
        """test question posted by user already exist (409)"""
        pass
    
    def test_3_get_specific_question(self):
        """user should be able to get a specific questions so as to upvote or downvote (200)"""
        pass

    def test_4_user_upvote_question(self):
        """test user upvote a question succesfully (204)"""
        pass
    
    def test_5_user_downvote(self):
        """test user downvotes a question succesfully (204)"""
        pass
    
    """test validations"""
    def test_question_exist(self):
        """test that question exist when user inputs it twice (409)"""
        pass
    
    def test_id_not_found(self):
        """check when question id is missing (404)"""
        pass
    
   
    
    