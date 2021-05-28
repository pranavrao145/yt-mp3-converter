from flask import Flask
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app, start_server="flask")

from application import routes
