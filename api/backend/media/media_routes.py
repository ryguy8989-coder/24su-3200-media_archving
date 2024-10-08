from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict



# make blueprint object
media= Blueprint('media ids', __name__)

# Route to create new video
@media.route('/videos', methods=['POST'])
def create_video():
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting variables from the request data
    id = the_data.get('id')
    length = the_data.get('length')
    description = the_data.get('description')
    video_type = the_data.get('video_type')
    name = the_data.get('name')
    size = the_data.get('size')
    quality = the_data.get('quality')
    genre = the_data.get('genre')
    director = the_data.get('director')

    query = '''
        INSERT INTO media_videos 
        (id, length, description, video_type, name, size, quality, genre, director) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query, (id, length, description, video_type, name, size, quality, genre, director))
    db.get_db().commit()

    return jsonify({"message": "Video created successfully!"}), 201


# Route to create new literature
@media.route('/literature', methods=['POST'])
def create_literature():
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting variables from the request data
    id = the_data.get('id')
    link = the_data.get('link')
    description = the_data.get('description')
    type = the_data.get('type')
    title = the_data.get('title')
    publisher = the_data.get('publisher')
    publication_date = the_data.get('publication_date')
    genre = the_data.get('genre')
    author = the_data.get('author')
    page_count = the_data.get('page_count')
    ISBN = the_data.get('ISBN')
    budget = the_data.get('budget')

    query = '''
        INSERT INTO media_literature
        (id, link, description, type, title, publisher, publication_date, genre, author, page_count, ISBN, budget) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query, (id, link, description, type, title, publisher, publication_date, 
                           genre, author, page_count, ISBN, budget))
    db.get_db().commit()

    return jsonify({"message": "Literature created successfully!"}), 201

# Route for admin to create new media image
@media.route('/images', methods=['POST'])
def create_new_image():
    try:
        data = request.get_json()
        id = data.get('id')
        image_type = data.get('image_type')
        image_link = data.get('image_link')
        photographer = data.get('photographer')
        title = data.get('title')
        description = data.get('description')
        if not image_type or not image_link or not photographer or not title or not description:
            return jsonify({'error': 'Missing required fields'}), 400
        cursor = db.get_db().cursor()
        query = """
            INSERT INTO media_images (id, image_type, image_link, photographer, title, description)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (id, image_type, image_link, photographer, title, description))
        db.get_db().commit()
        cursor.close()
        return jsonify({'message': 'Media image added successfully'}), 201
    except Exception as e:
        current_app.logger.error(f'Error finding media image: {e}')
        return jsonify({'error': 'An error occurred while updating media image'}), 500


#method to add media to users in bridge table
@media.route('/user_media', methods=['POST'])
def add_user_media():
    try:
        # Get the data from the request
        input = request.get_json()
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
    
#method to add tags to media in bridge table
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
            return jsonify({"error": "Both tag_id and media_id are required"}), 400

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
    

    



    
