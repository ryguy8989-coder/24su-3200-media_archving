########################################################
# Sample employees blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
videos= Blueprint('videos', __name__)

# Make route to get all videos
@videos.route('/videos', methods=['GET'])
def get_all_videos():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM media_videos 

'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@videos.route('/videos', methods=['GET'])
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