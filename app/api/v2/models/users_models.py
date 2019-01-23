"""
user database connection and  model 
"""
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from app.api.v2.models.database import init_db
from app.api.v2.models.basemodel import BaseModel

class UserModel(BaseModel):
    """This class encapsulates the functions of the user model"""

    def __init__(self, firstname="firstname", lastname="lastname", email="@mail.com", password="pass",confirm_password="pass", phonenumber="1233", username="user"):
        """initialize the user model"""
        self.db = init_db()
        """user data"""
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
        curr = self.db.cursor()
        query = "SELECT  username FROM users WHERE username = '%s'" % (username)
        curr.execute(query)
        return curr.fetchone() is not None
    """check if user email already exist or not"""
    def check_email_exist(self, email):
        """checks if email already exists"""
        curr = self.db.cursor()
        query = "SELECT  email FROM users WHERE email = '%s'" % (email)
        curr.execute(query)
        return curr.fetchone() is not None
    
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
        database = self.db
        cur = database.cursor()
        query = """INSERT INTO users (firstname, lastname, email, passwor, confirm_password, registered, phonenumber, username, isAdmin) \
            VALUES (%(firstname)s, %(lastname)s, %(email)s, %(password)s, %(confirm_password)s, %(registered)s, %(phonenumber)s, %(username)s, %(isAdmin)s)
            RETURNING id, registered;
            """
        cur.execute(query, user)
        print("inserted")
        user_id = cur.fetchone()[0]
        database.commit()
        cur.close()
        return int(user_id)

      #log in user
    
    """user sign in"""
    def login_user(self, email):
        """searches for a single user by use of email"""
        """return user from the db given a username"""
        database = self.db
        curr = database.cursor()
        curr.execute(
            """SELECT id, firstname, lastname, passwor,registered
            FROM users WHERE email = '%s'""" % (email))
        data = curr.fetchone()
        curr.close()
        return data