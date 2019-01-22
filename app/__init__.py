from flask import Flask

# local import
from instance.config import app_config
from app.api import version_two as questioner_two

create_app = Flask(__name__)

create_app.register_blueprint(questioner_two, url_prefix="api/v2")
