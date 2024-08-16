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
     SELECT * FROM media_literature  
'''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@lit.route('lit/<tag>', methods=['GET'])
def get_media_literature_by_tag(tag):
    current_app.logger.info('GET /lit/{tag} route')
    cursor = db.get_db().cursor()
    # Query to find media literature by tag
    query = f"""
        SELECT ml.*
        FROM media_literature ml
        JOIN media_tags mt ON ml.id = mt.media_id
        JOIN tags t ON mt.tag_id = t.tag_id
        WHERE t.tag_name = '{tag}'
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