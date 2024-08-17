########################################################
# Sample media images blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

# make blueprint object
find_media= Blueprint('find_media', __name__)

# Make route
@find_media.route('/images', methods=['GET'])
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

# Make route
@find_media.route('/lit', methods=['GET'])
def get_all_media_literature():
    cursor = db.get_db().cursor()
    query = '''
     SELECT * FROM media_literature  
'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Make route to get all videos
@find_media.route('/videos', methods=['GET'])
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



# Get all Media IDs
@find_media.route('/media_ids', methods=['GET'])
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


# Make route
@find_media.route('/media_tags', methods=['GET'])
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

