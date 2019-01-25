# inbuilt modules
import re
import os
from functools import wraps
# third party modules
from flask import jsonify, request, make_response, abort

class CheckData:
    @staticmethod
    def checkkey(data):
        for key, value in data.items():
            if key == "firstname" or key == "lastname" or key == "username":
                for i in key:
                    if "0-9@_+-." in i:
                        return make_response(jsonify({"message":"firstname,lastname and username should not contain 0-9@_+-."}),400)                
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

