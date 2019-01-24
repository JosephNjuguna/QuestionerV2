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
        password VARCHAR(100) NOT NULL,
        confirm_password VARCHAR(100) NOT NULL,
        registered TIMESTAMP,
        phonenumber VARCHAR(12) NOT NULL,
        username VARCHAR(12) NOT NULL,
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

def drop_existing_tables():
    users_table = """ DROP TABLE IF EXISTS users """
    meetups_table = """ DROP TABLE IF EXISTS meetups """
    questions_table = """ DROP TABLE IF EXISTS questions """
    comments_table= """ DROP TABLE IF EXISTS comments """
    rsvp_table = """ DROP TABLE IF EXISTS rsvp """
    votes_table = """ DROP TABLE IF EXISTS votes """

    return [votes_table, rsvp_table, comments_table, meetups_table, questions_table, users_table]

def drop_tables(connect):
    queries = drop_existing_tables()
    cur = connect.cursor()
    for query in queries:
        cur.execute(query)
    connect.commit()
    cur.close()
    connect.close()

def create_admin(connect):
    query = """INSERT INTO users (
            firstname, lastname, username, email, phonenumber, password, confirm_password, registered, isAdmin) 
    VALUES( '{}', '{}','admin','adm@admn.com','07012345678', '{}', '{}', '1/1/2018','true')""".format(
            'admin', 'super', 'admin', generate_password_hash("$$PAss12"))
    get_admin = """SELECT * from users WHERE username = 'admin'"""
    cur = connect.cursor()
    get_admin = cur.execute(get_admin)
    get_admin = cur.fetchone()
    if get_admin:
        pass
    else:
        cur.execute(query)
        connect.commit()
