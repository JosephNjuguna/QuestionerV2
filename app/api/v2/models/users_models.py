"""
user database connection and  model 
"""
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from app.api.v2.models.basemodel import DatabaseConnection as connection

class UserModel(connection):
    """This class encapsulates the functions of the user model"""

    def __init__(self, firstname="firstname", lastname="lastname", email="@mail.com", password="pass",confirm_password="pass", phonenumber="1233", username="user",public_id=""):
        """create instance of user model"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.confirm_password= generate_password_hash(confirm_password, method='sha256')
        self.phonenumber = phonenumber
        self.username = username
        self.isAdmin = False
        self.public_id = public_id
    
    """validate if user data exist or not(inheried by add user"""
    def check_user_exist(self, username):
        """checks if user already exists"""
        query = "SELECT  username FROM users WHERE username = '%s'" % (username)
        result = self.fetch_single_data_row(query)
        return result

    """check if user email already exist or not"""
    def check_email_exist(self, email):
        """checks if email already exists"""
        query = "SELECT  email FROM users WHERE email = '%s'" % (email)
        result = self.fetch_single_data_row(query)
        return result
    
    """sign up user"""
    def add_user(self):        
        """check if user exists"""
        if self.check_user_exist(self.username):
            return True

        if self.check_email_exist( self.email):
            return True
            
        # check if user exists
        query = """INSERT INTO users(firstname, lastname, email, user_password, confirm_password,phonenumber, username, public_id, isAdmin) 
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')RETURNING public_id;""".format(self.firstname, self.lastname, self.email, self.password,self.confirm_password, self.phonenumber, self.username, self.public_id, self.isAdmin)
        result = self.save_incoming_data_or_updates(query)
        return result
    
    def login_user(self, email):
        """user sign in"""
        query =("""SELECT user_password,public_id
        FROM users WHERE email = '%s' """ %(email))
        data = self.fetch_single_data_row(query)
        return data