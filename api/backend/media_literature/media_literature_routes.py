from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
lit= Blueprint('lit', __name__)

# Make route
@lit.route('/lit', methods=['GET'])
def get_all_media_literature():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM media literature  
'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response