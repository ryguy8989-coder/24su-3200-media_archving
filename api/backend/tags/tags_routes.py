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

@tags.route('/videos', methods=['GET'])
def find_tagged_videos():
    # Get the tag name from the query parameters
    tag_name = request.args.get('tag', default='', type=str)

    if not tag_name:
        return jsonify({"error": "Tag name is required"}), 400

    cursor = db.get_db().cursor()
    query = '''
     SELECT mv.name, mv.genre, mv.director, t.tag_name
     FROM media_videos mv
     JOIN media_tags mt ON mv.id = mt.media_id
     JOIN tags t ON mt.tag_id = t.tag_id
     WHERE t.tag_name = %s
     ORDER BY mv.name ASC;
    '''
    cursor.execute(query, (tag_name,))
    theData = cursor.fetchall()

    # Check if data is found
    if not theData:
        return jsonify({"message": "No videos found for the provided tag"}), 404

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@tags.route('/literature', methods=['GET'])
def find_tagged_literature():
    tag_name = request.args.get('tag', default='', type=str)

    if not tag_name:
        return jsonify({"error": "Tag name is required"}), 400

    cursor = db.get_db().cursor()
    query = '''
    SELECT ml.title, ml.author, ml.genre, t.tag_name
    FROM media_literature ml
    JOIN media_tags mt ON ml.id = mt.media_id
    JOIN tags t ON mt.tag_id = t.tag_id
    WHERE t.tag_name = %s
    ORDER BY ml.title ASC;
    '''
    cursor.execute(query, (tag_name,))
    rows = cursor.fetchall()

    # Convert fetched data to a list of dictionaries
    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in rows]

    return jsonify(data), 200