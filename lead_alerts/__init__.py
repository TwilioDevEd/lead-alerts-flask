from flask import Flask
import os

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
app.secret_key = os.environ.get('SECRET_KEY', None)

import lead_alerts.views
