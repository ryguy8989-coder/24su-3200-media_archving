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

@tags.route('tags/trending', methods=['GET'])
def get_trending_tags():
    cursor = db.get_db().cursor()
    
    #query to find trending tags
    query = '''
        SELECT t.tag_name, COUNT(mt.tag_id) AS usage_count
        FROM tags t
        JOIN media_tags mt ON t.tag_id = mt.tag_id
        GROUP BY t.tag_name
        ORDER BY usage_count DESC
        LIMIT 10;
    '''
    cursor.execute(query)
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

#  Delete a Tag
@tags.route('/tags', methods=['DELETE'])
def delete_tag_by_name():
    tag_name = request.args.get('tag_name', default='', type=str)

    if not tag_name:
        return jsonify({"error": "Tag name is required"}), 400

    cursor = db.get_db().cursor()

    # Delete the tag
    query_delete = 'DELETE FROM tags WHERE tag_name = %s'
    cursor.execute(query_delete, (tag_name,))
    db.get_db().commit()

    return jsonify({"message": f"Tag '{tag_name}' deleted successfully"}), 200

#updating tags
@tags.route('/tags', methods = ['PUT'])
def update_tag():
    # Get the JSON data from the request
    tag_info = request.json
    current_app.logger.info(tag_info)

    # Extract the relevant data from the request
    old_tag_name = tag_info.get('old_tag_name')
    new_tag_name = tag_info.get('new_tag_name')

    if not old_tag_name or not new_tag_name:
        return jsonify({"error": "Both old_tag_name and new_tag_name are required"}), 400

    cursor = db.get_db().cursor()
    
    # Update the tag name
    query_update = 'UPDATE tags SET tag_name = %s WHERE LOWER(tag_name) = LOWER(%s)'
    cursor.execute(query_update, (new_tag_name, old_tag_name))
    db.get_db().commit()

    return jsonify({"message": f"Tag '{old_tag_name}' updated successfully to '{new_tag_name}'"}), 200
