from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import Config

app = Flask(__name__)

# create database instance
db = SQLAlchemy(app)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# import done here because routes requires app to be initialized to work
# watch out for circular imports!!!
from flaskblog import routes