from flask_restful import Resource

class SignUp(Resource):
    """user sign up endpoint"""
    def __init__(self):
        pass
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