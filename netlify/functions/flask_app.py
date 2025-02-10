# netlify/functions/flask_app.py
import os
import sys

# Insert the root folder into sys.path so that app.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app import app
from serverless_wsgi import handle_request

def handler(event, context):
    return handle_request(app, event, context)
