########################################################
# Sample media images blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
images= Blueprint('images', __name__)

# Make route
@images.route('/images', methods=['GET'])
def get_all_images():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM media_images  

'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@images.route('/images/<tag>', methods=['GET'])
def get_images_by_tag(tag):
    current_app.logger.info('GET /images/{tag} route')
    cursor = db.get_db().cursor()

    # Query to find media images by tag
    query  = f"""
        SELECT mi.id, mi.image_type, mi.image_link, mi.photographer, mi.title, mi.description
        FROM media_images mi
        JOIN media_tags mt ON mi.id = mt.media_id
        JOIN tags t ON mt.tag_id = t.tag_id
        WHERE t.tag_name = '{tag}';
        """
    cursor.execute(query)

    rows = cursor.fetchall()
    cursor.close()

    # Convert rows to JSON
    json_data = [dict(row) for row in rows]
    response = make_response(jsonify(json_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response