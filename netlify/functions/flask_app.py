# netlify/functions/flask_app.py
from flask import Flask, jsonify
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run()
