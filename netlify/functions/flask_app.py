import os
import sys

# Adjust the path so that the repository root is available.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app import app
from serverless_wsgi import handle_request

def handler(event, context):
    return handle_request(app, event, context)