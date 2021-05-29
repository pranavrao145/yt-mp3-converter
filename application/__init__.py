from flask import Flask
from flaskwebgui import FlaskUI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
ui = FlaskUI(app, start_server="flask")

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

from application import routes
