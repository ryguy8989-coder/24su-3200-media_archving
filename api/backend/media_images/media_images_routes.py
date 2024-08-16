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
    
# Route for admin to create new media image
@images.route('/images', methods=['POST'])
def create_new_image():
    try:
        data = request.get_json()
        image_type = data.get('image_type')
        image_link = data.get('image_link')
        photographer = data.get('photographer')
        title = data.get('title')
        description = data.get('description')
        if not image_type or not image_link or not photographer or not title or not description:
            return jsonify({'error': 'Missing required fields'}), 400
        cursor = db.get_db().cursor()
        query = """
            INSERT INTO media_images (image_type, image_link, photographer, title, description)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (image_type, image_link, photographer, title, description))
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Media image added successfully'}), 201


# Route for admin to update existing media image
@images.route('/images/<int:id>', methods=['PUT'])
def update_image(id):
    try:
        data = request.get_json()
        image_type = data.get('image_type')
        image_link = data.get('image_link')
        photographer = data.get('photographer')
        title = data.get('title')
        description = data.get('description')
        if not image_type or not image_link or not photographer or not title or not description:
            return jsonify({'error': 'Missing required fields'}), 400
        cursor = db.get_db().cursor()
        query = """
            UPDATE media_images
            SET image_type = %s, image_link = %s, photographer = %s, title = %s, description = %s
            WHERE id = %s
        """
        cursor.execute(query, (image_type, image_link, photographer, title, description, id))
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Media image updated successfully'}), 200
    except Exception as e:
        current_app.logger.error(f'Error updating media image: {e}')
        return jsonify({'error': 'An error occurred while updating media image'}), 500


# Route for admin to delete existing media image
@images.route('/images/<int:id>', methods=['DELETE'])
def delete_image(id):
    try:
        cursor = db.get_db().cursor()
        query = "DELETE FROM media_images WHERE id = %s"
        cursor.execute(query, (id,))
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Media image deleted successfully'}), 200
    except Exception as e:
        current_app.logger.error(f'Error deleting media image: {e}')
        return jsonify({'error': 'An error occurred while deleting media image'}), 500
