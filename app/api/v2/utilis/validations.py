# inbuilt modules
import re
import os
from functools import wraps
# third party modules
from flask import jsonify, request, make_response, abort

class CheckData:
    @staticmethod
    def checkkey(data):
        for k, v in data.items():
            if len(v)== 0:
                return make_response(jsonify({"message":"empty field"}))

class AuthValidation:
    """Validators Class"""

    @staticmethod
    def validate_username(username):
        """validate username"""
        regex = "^[a-zA-Z]{3,}$"
        if re.match(regex,username):
            return True

    @staticmethod
    def validate_email(email):
        """ valid email """
        regex = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        if re.match(regex, email):
            return True

    @staticmethod
    def validate_password(password):
        """ valid password """
        regex = "^[a-zA-Z0-9@_+-.]{5,}$"
        if re.match(regex, password):
            return True

    @staticmethod
    def check_password_match(password, confirm_password):
        if confirm_password != password:
            return True

