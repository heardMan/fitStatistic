import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from models import setup_db, seed_db, User

app = Flask(__name__)

setup_db(app)
seed_db()

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():

    query1 = User.query.all()
    print(query1[0].roles[0].role_definition)
    
    return jsonify({
        'success': True,
        'message': 'Welcome to fitStatistic API! Feel free to check out our docs on github!',
        'link':'https://github.com/heardMan/fitStatistic'
    }), 200

@app.route('/auth', methods=['POST'])
def authenticate():

    token = 'token'


    return jsonify({
        'success': True,
        'message': 'Success',
        'token': token
    }), 200

if __name__ == '__main__':
    app.run()