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

@videos.route('videos/<genre>', methods=['GET'])
def get_video_genre(genre):
    current_app.logger.info('GET /videos/{genre} route')
    cursor = db.get_db().cursor()
    query = f"SELECT * FROM media_videos WHERE genre = '{genre}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    cursor.close()

    # Convert rows to JSON
    json_data = [row for row in rows]
    response = make_response(jsonify(json_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

# Route for admin to add a new video
@videos.route('/videos', methods=['POST'])
def add_video():
    data = request.get_json()
    title = data.get('title')
    genre = data.get('genre')
    description = data.get('description')
    url = data.get('url')
    if not title or not genre or not description or not url:
        return jsonify({'error': 'Missing required fields'}), 400
    cursor = db.get_db().cursor()
    query = '''
        INSERT INTO media_videos (title, genre, description, url)
        VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(query, (title, genre, description, url))
    db.get_db().commit()
    cursor.close()

    return jsonify({'message': 'Video added successfully'}), 201

# Route for admin to update an existing video
@videos.route('/videos/<int:video_id>', methods=['PUT'])
def update_video(video_id):
    data = request.get_json()
    title = data.get('title')
    genre = data.get('genre')
    description = data.get('description')
    url = data.get('url')

    cursor = db.get_db().cursor()
    query = '''
        UPDATE media_videos
        SET title = %s, genre = %s, description = %s, url = %s
        WHERE id = %s
    '''
    cursor.execute(query, (title, genre, description, url, video_id))
    db.get_db().commit()
    cursor.close()

    return jsonify({'message': 'Video updated successfully'}), 200

# Route for admin to delete a video
@videos.route('/videos/<int:video_id>', methods=['DELETE'])
def delete_video(video_id):
    cursor = db.get_db().cursor()
    query = 'DELETE FROM media_videos WHERE id = %s'
    cursor.execute(query, (video_id,))
    db.get_db().commit()
    cursor.close()

    return jsonify({'message': 'Video deleted successfully'}), 200
