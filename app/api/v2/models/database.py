#inbuilt modules
import os
#downloaded module
from flask import current_app
#local imports
import psycopg2, psycopg2.extras

def create_tables():
        #users table
        users_table ='''CREATE TABLE IF NOT EXISTS users (
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
            '''
        #meetup table
        meetup_table ='''CREATE TABLE IF NOT EXISTS meetup (
            id serial PRIMARY KEY,
            createdon TIMESTAMP,
            venue VARCHAR(100) NOT NULL,
            topic VARCHAR(100) NOT NULL,
            happening VARCHAR(100) NOT NULL,
            tags VARCHAR(30) NOT NULL);
            '''
        #question table
        question_table ='''CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            createdon VARCHAR NOT null,
            postedby INT NOT NULL,
            meetupid INT NOT NULL,
            title VARCHAR(40) NOT NULL,
            body VARCHAR(200) NOT NULL,
            votes  INT NOT NULL);
            '''
        rsvp_table= '''CREATE TABLE IF NOT EXISTS rsvp(
            id SERIAL PRIMARY KEY,
            rsvpdate VARCHAR NOT null,
            topic VARCHAR(40) NOT NULL,
            userstatus VARCHAR(5) NOT NULL,
            username VARCHAR NOT NULL);
            '''
        return [users_table,question_table, meetup_table, rsvp_table]
    
        
def init_db():
    tables= create_tables()
    """connection to db"""
    conn = psycopg2.connect("dbname='questioner' user='alan'")
    cur = conn.cursor()
    for query in tables:
        cur.execute(query)
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