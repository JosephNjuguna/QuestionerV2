#inbuilt modules
import os
#import datetime
#downloaded module
from flask_restful import Resource
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
#local imports
from app.api.v2.models.users_models import UserModel
from app.api.v2.utilis.validations import (CheckData, AuthValidation)
from app.api.v2.utilis.error_handler import RaiseErrors

data_validation = CheckData()
info_validation = AuthValidation()

class SignUp(Resource):
    """user sign up endpoint"""
    @staticmethod
    def post():
            data = request.get_json()
            data_state = data_validation.checkkey(data)

            firstname = data["firstname"]
            lastname = data["lastname"]
            email = data["email"]
            password = data["password"]
            confirm_password = data["confirm_password"]
            phonenumber = data["phone"]
            username = data["username"]
            token = ""

            """check user name length"""
            name = info_validation.validate_username(username)
            if not name:
                return RaiseErrors.username_short()

            """check email format"""
            check_email = info_validation.validate_email(email)
            if not check_email:
                return RaiseErrors.invalid_email()
            
            """check password length"""
            check_length = info_validation.validate_password(password)
            if not check_length:
                return RaiseErrors.password_validity()

            """check password match"""
            password_check = info_validation.check_password_match(password, confirm_password)
            if password_check:
                return RaiseErrors.password_match()

            user= {
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "password" : password,
                "confirm_password" : confirm_password,
                "phonenumber":phonenumber,
                "username" : username
            }
            user_data = UserModel(**user)
            saved = user_data.add_user()
            user_id = saved
            resp = {
                "status":201,
                "data": [{
                    "user_id": "{}".format(user_id),
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname
                }]
            }
            return resp
class LogIn(Resource):
    """user log in endpoint"""
    @staticmethod
    def post():
        try:
            data = request.get_json()
            data_state = data_validation.checkkey(data)
            
            email = data['email']
            password = data['password']

            """check email format"""
            check_email = info_validation.validate_email(email)
            if not check_email:
                return RaiseErrors.invalid_email()

            """check password length"""
            check_length = info_validation.validate_password(password)
            if not check_length:
                return RaiseErrors.password_validity()

            user_details= {
                "email":email,
                "password": password
            }
            #pass user data to db
            user = UserModel(**user_details)

            #check user exist
            check_user_data = user.login_user(user_details["email"])
            if not check_user_data:
                return 'Your details were not found, please sign up',400
            user_id, fname, lname, pwordhash, date_created = check_user_data
            if check_password_hash(pwordhash, user_details["password"]):
                name = "{}, {}".format(lname, fname)
                resp = dict(
                    message="successful log in",
                    name= name,
                    date_created=str(date_created)
                )
                return resp, 200    
            return "The password is incorrect",400
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}), 500)
    
class OneUser(Resource):
    """get one user endpoint"""
    def __init__(self):
        pass
class UserUpdateInfo(Resource):
    """user can update their information"""
    def __init__(self):
        pass
class UserResetPassword(Resource):
    """ a user can reset their password"""
    def __init__(self):
        pass