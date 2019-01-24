import os
import psycopg2
from flask import Flask
from instance.config import app_config
from app.api import version_two as questioner_two
from app.api.v2.models.basemodel import DatabaseConnection

def create_app(name_conf):
    my_app = Flask(__name__, instance_relative_config=True)
    my_app.config.from_object(app_config[name_conf])
    my_app.config.from_pyfile('config.py')

    db_url = app_config[name_conf].Database_Url

    DatabaseConnection(db_url)
    if name_conf == "testing":
        DatabaseConnection.drop_all_tables(DatabaseConnection)
    DatabaseConnection.create_tables_and_admin(DatabaseConnection)

    my_app.register_blueprint(questioner_two, url_prefix="/api/v2")
 
    return my_app