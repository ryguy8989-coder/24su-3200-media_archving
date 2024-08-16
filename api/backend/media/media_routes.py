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


@media.route('/user_media', methods=['POST'])
def add_user_media():
    try:
        # Get the data from the request
        input = request.json
        current_app.logger.info(input)

        # Extract the necessary information
        user_id = input.get('user_id')
        media_id = input.get('media_id')

        # Validate that both user_id and media_id are provided
        if not user_id or not media_id:
            return jsonify({"error": "Both user_id and media_id are required"}), 400

        # Construct the SQL query to insert into user_media table
        query = '''
            INSERT INTO user_media (user_id, media_id)
            VALUES (%s, %s)
        '''

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (user_id, media_id))
        db.get_db().commit()

        return jsonify({"message": "Media added to user successfully!"}), 201

    except Exception as e:
        current_app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": "Failed to add media to user"}), 500
    

@media.route('/add_media_tag', methods=['POST'])
def add_media_tag():
    try:
        # Get the data from the request
        input = request.json
        current_app.logger.info(input)

        # Extract the necessary information
        tag_id = input.get('tag_id')
        media_id = input.get('media_id')

        # Validate that both tag_d and media_id are provided
        if not tag_id or not media_id:
            return jsonify({"error": "Both user_id and media_id are required"}), 400

        # Construct the SQL query to insert into media_tags table
        query = '''
            INSERT INTO media_tags (tag_id, media_id)
            VALUES (%s, %s)
        '''

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (tag_id, media_id))
        db.get_db().commit()

        return jsonify({"message": "Tag added to media successfully!"}), 201

    except Exception as e:
        current_app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": "Failed to add tag to media"}), 500
    

    



    
