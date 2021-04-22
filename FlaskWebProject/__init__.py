"""
The flask application package.
"""

#from FlaskWebProject import views


import FlaskWebProject.views
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.WARNING)
my_handler = logging.StreamHandler()
my_handler.setLevel(logging.WARNING)
app.logger.addHandler(my_handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'