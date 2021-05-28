from flask import Flask
from flaskwebgui import FlaskUI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
ui = FlaskUI(app, start_server="flask")

from application import routes
