########################################################
# Sample users blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
users = Blueprint('users', __name__)

# Make route
@users.route('/users', methods=['GET'])
def get_all_users():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM users 

'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response