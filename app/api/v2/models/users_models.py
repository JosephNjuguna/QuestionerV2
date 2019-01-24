"""
user database connection and  model 
"""
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from app.api.v2.models.basemodel import DatabaseConnection as connection

class UserModel(connection):
    """This class encapsulates the functions of the user model"""

    def __init__(self, firstname="firstname", lastname="lastname", email="@mail.com", password="pass",confirm_password="pass", phonenumber="1233", username="user"):
        """create instance of user model"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password)
        self.confirm_password= generate_password_hash(confirm_password)
        self.registered =str(datetime.datetime.utcnow())
        self.phonenumber = phonenumber
        self.username = username
        self.isAdmin = False
    
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
        """Add user details to the database"""
        user = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "confirm_password":self.confirm_password,
            "registered": self.registered,
            "phonenumber":self.phonenumber,
            "username":self.username,
            "isAdmin":self.isAdmin
        }
        """check if user exists"""
        if self.check_user_exist(user['username']):
            return "User exist"

        if self.check_email_exist( user['email']):
            return "email exist"
            
        # check if user exists
        query = """INSERT INTO users(firstname, lastname, email, password, confirm_password, registered, phonenumber, username, isAdmin) 
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')RETURNING id, registered;""".format(self.firstname,self.lastname,self.email,self.password,self.confirm_password,self.registered, self.phonenumber, self.username, self.isAdmin)
        result = self.save_incoming_data_or_updates(query)
        return result
    
    def login_user(self, email):
        """user sign in"""
        query =("""SELECT id, firstname, lastname,password,registered 
        FROM users WHERE email = '%s' """ % (email))
        data = self.fetch_single_data_row(query)
        return data