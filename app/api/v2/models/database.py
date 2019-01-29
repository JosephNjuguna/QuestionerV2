import os
import sys
import datetime
import uuid
from flask import abort, make_response, jsonify
from werkzeug.security import generate_password_hash
import psycopg2
from instance.config import app_config

def create_tables():
    """users table"""
    users_table = '''CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        firstname VARCHAR(16) NOT NULL,
        lastname VARCHAR(16) NOT NULL,
        email VARCHAR(30) NOT NULL,
        user_password VARCHAR(100) NOT NULL,
        confirm_password VARCHAR(100) NOT NULL,
        registered TIMESTAMP,
        phonenumber VARCHAR(12) NOT NULL,
        username VARCHAR(12) NOT NULL,
        public_id VARCHAR(50) NOT NULL,
        isAdmin VARCHAR(10) NOT NULL);
        '''
    """meetup table"""
    meetup_table = '''CREATE TABLE IF NOT EXISTS meetup (
        id serial PRIMARY KEY,
        createdon VARCHAR(30) NOT NULL,
        venue VARCHAR(100) NOT NULL,
        topic VARCHAR(100) NOT NULL,
        happening VARCHAR(100) NOT NULL,
        tags VARCHAR(30) NOT NULL);
        '''
    """question table"""
    question_table = '''CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        createdon VARCHAR NOT null,
        postedby INT NOT NULL,
        meetupid INT NOT NULL,
        questionid VARCHAR NOT NULL,
        title VARCHAR(40) NOT NULL,
        body VARCHAR(200) NOT NULL,
        votes  INT NOT NULL);
        '''
    """comments table"""
    comments_table = '''CREATE TABLE IF NOT EXISTS comments(
        id SERIAL PRIMARY KEY,
        createdon VARCHAR NOT null,
        postedby INT NOT NULL,
        questionid INT NOT NULL,
        body VARCHAR(200) NOT NULL);
        '''
    rsvp_table= '''CREATE TABLE IF NOT EXISTS rsvp(
        id SERIAL PRIMARY KEY,
        rsvpdate VARCHAR NOT null,
        topic VARCHAR(40) NOT NULL,
        userstatus VARCHAR(5) NOT NULL,
        username VARCHAR NOT NULL);
        '''
    return [users_table,question_table, meetup_table, rsvp_table,comments_table]
         
def init_db():
    tables= create_tables()
    """connection to db"""
    conn = psycopg2.connect("dbname='questioner' user='alan'")
    cur = conn.cursor()
    for query in tables:
        cur.execute(query)
    return conn

def drop_existing_tables():
    users_table = """ DROP TABLE IF EXISTS users """
    meetups_table = """ DROP TABLE IF EXISTS meetups """
    questions_table = """ DROP TABLE IF EXISTS questions """
    comments_table= """ DROP TABLE IF EXISTS comments """
    rsvp_table = """ DROP TABLE IF EXISTS rsvp """

    return [rsvp_table, comments_table, meetups_table, questions_table, users_table]

def drop_tables(connect):
    queries = drop_existing_tables()
    cur = connect.cursor()
    for query in queries:
        cur.execute(query)
    connect.commit()
    cur.close()
    connect.close()

def create_admin(connect):
    query = """INSERT INTO users (firstname, lastname,  email, user_password, confirm_password, phonenumber, username, public_id, isAdmin) 
    VALUES('{}','{}','{}','{}','{}','0712345678','admin','{}','True')""".format('admin','super','adm@admn.com', generate_password_hash("189@admin",method='sha256'), generate_password_hash("189@admin",method='sha256'),uuid.uuid4())
    
    get_admin = """SELECT * from users WHERE username = 'admin'"""
    cur = connect.cursor()
    get_admin = cur.execute(get_admin)
    get_admin = cur.fetchone()
    if get_admin:
        pass
    else:
        cur.execute(query)
        connect.commit()
