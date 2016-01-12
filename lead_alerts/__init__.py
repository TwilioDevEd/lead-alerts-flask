from flask import Flask

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')

import lead_alerts.views
