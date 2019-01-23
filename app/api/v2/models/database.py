#inbuilt modules
import os
#downloaded module
from flask import current_app
#local imports
import psycopg2

def init_db():
    #users table
    users_table = ('''CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            firstname VARCHAR(16) NOT NULL,
            lastname VARCHAR(16) NOT NULL,
            email VARCHAR(30) NOT NULL,
            passwor VARCHAR(100) NOT NULL,
            confirm_password VARCHAR(100) NOT NULL,
            registered TIMESTAMP,
            phonenumber VARCHAR(12) NOT NULL,
            username VARCHAR(12) NOT NULL,
            isAdmin VARCHAR(10) NOT NULL);
            ''')
    print("users")
    #meetup table
    meetup_table = ('''CREATE TABLE IF NOT EXISTS meetup (
            id serial PRIMARY KEY,
            createdon TIMESTAMP,
            venue VARCHAR(100) NOT NULL,
            topic VARCHAR(100) NOT NULL,
            happening VARCHAR(100) NOT NULL,
            tags VARCHAR(30) NOT NULL);
            ''')
    print("meetup")
    #question table
    question_table = ('''CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            createdon VARCHAR not null,
            postedby INT NOT NULL,
            meetupid INT NOT NULL,
            title VARCHAR(40) NOT NULL,
            body VARCHAR(200) NOT NULL,
            votes  INT NOT NULL);
            ''')
    
    """connection to db"""
    conn = psycopg2.connect("dbname='questioner' user='alan'")
    cur = conn.cursor()
    cur.execute(question_table)
    cur.execute(meetup_table)
    cur.execute(users_table)
    return conn

def _init_db():
    conn = psycopg2.connect("dbname='questionertest' user='alan'")
    cur = conn.cursor()
    destroy()
    return conn

def connect_to(url):
    conn = psycopg2.connect(url)
    return conn

def destroy():
    test_url = os.getenv('DATABASE_TEST_URL')
    conn = connect_to(test_url)
    curr = conn.cursor()
    users = "DROP TABLE IF EXISTS users "
    meetup = "DROP TABLE IF EXISTS users "
    questioner = "DROP TABLE IF EXISTS users "
    queries = [users,meetup,questioner]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        print("Fail")