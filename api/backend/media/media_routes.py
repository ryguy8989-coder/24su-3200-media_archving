from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
media= Blueprint('media ids', __name__)

# Make route
@media.route('/media_ids', methods=['GET'])
def get_all_media_ids():
    cursor = db.get_db().cursor()
    query = '''
     SELECT media_id FROM media   
'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# make blueprint object
media_tags= Blueprint('media_tags', __name__)

# Make route
@media.route('/media_tags', methods=['GET'])
def get_all_media_tags():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM media_tags 

'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

