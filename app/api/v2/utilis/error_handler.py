from flask import make_response,jsonify

class RaiseErrors():
    @staticmethod
    def username_short():
        return make_response(jsonify({"message": "username too short"}),400)

    @staticmethod
    def invalid_email():
        return make_response(jsonify({"message": "invalid email"}),400)

    @staticmethod
    def password_validity():
        return make_response(jsonify({"message": "invalid password"}),400)

    @staticmethod
    def password_match():
        return make_response(jsonify({"message": "password mismatch"}),400)

