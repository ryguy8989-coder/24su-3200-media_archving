########################################################
# Sample tags blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
tags= Blueprint('tags', __name__)

# Make route
@tags.route('/tags', methods=['GET'])
def get_all_tags():
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of tags
    cursor.execute('SELECT * FROM tags ORDER BY tag_id ASC;')

    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Route to create a new tag
@tags.route('/tags', methods=['POST'])
def create_tag():
    #collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    #Extracting the variable
    
    name = the_data['tag_name']

    # Constructing the query

    query = 'INSERT INTO tags (tag_name) VALUES ("{}")'.format(name)

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return jsonify({'message': 'Success!'}), 201