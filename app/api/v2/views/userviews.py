#inbuilt modules
import os
import datetime
import uuid
#downloaded modules
from flask_restful import Resource
from flask import request, jsonify, make_response
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from flask_jwt_extended import (JWTManager, verify_jwt_in_request, create_access_token,get_jwt_claims)
#local imports
from app.api.v2.models.users_models import UserModel
from app.api.v2.utilis.validations import (CheckData, AuthValidation)
from instance.config import app_config
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
            public_id = str(uuid.uuid4())

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
                "username" : username,
                "public_id": public_id
            }
            user_data = UserModel(**user)
            saved = user_data.add_user()
            user_id = saved
            access_token = create_access_token(user_id)
            resp = {
                "status":201,
                "data": [{
                    "token":access_token,
                    "username": username,
                    "firstname": firstname,
                    "lastname": lastname,
                }]
            }
            if saved != True:
                return  make_response(jsonify({"message":resp}),201)
            return make_response(jsonify({"message":"Username or email exist"}),409)
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
                "password":password
            }
            user = UserModel(email)
            check_user_data = user.login_user(user_details["email"])
            user_id, user_password = check_user_data    
            resp = {"user_id": check_user_data['public_id'], "user_email":email}
            if check_password_hash(check_user_data['user_password'],password):
                access_token = create_access_token(user_id)
                return make_response(jsonify({
                    "access_token": access_token,
                    "user_data":resp}),200)
            return make_response(jsonify({"message":"Invalid credentials"}),401)

        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}), 500)
