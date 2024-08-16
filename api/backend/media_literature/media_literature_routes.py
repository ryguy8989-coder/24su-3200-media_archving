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

# Route for admin to create new media literature
@lit.route('/lit', methods=['POST'])
def create_new_media_literature():
    try:
        data = request.get_json()
        title = data.get('title')
        genre = data.get('genre')
        description = data.get('description')
        author = data.get('author')
        publication_date = data.get('publication_date')

        # Validate required fields
        if not title or not genre or not description or not author or not publication_date:
            return jsonify({'error': 'Missing required fields'}), 400

        # Insert the new media literature into the database
        cursor = db.get_db().cursor()
        query = """
            INSERT INTO media_literature (title, genre, description, author, publication_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (title, genre, description, author, publication_date))
        db.get_db().commit()
        cursor.close()

        return jsonify({'message': 'Media literature added successfully'}), 201
    
    except Exception as e:
        current_app.logger.error(f'Error creating new media literature: {e}')
        return jsonify({'error': 'An error occurred while adding media literature'}), 500
