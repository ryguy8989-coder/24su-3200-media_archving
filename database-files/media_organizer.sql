DROP DATABASE IF EXISTS media_organizer;

CREATE DATABASE IF NOT EXISTS media_organizer;

USE media_organizer;

CREATE TABLE IF NOT EXISTS users
(
  user_id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  profile_pic_url VARCHAR(255),
  profile_bio TEXT,
  registration_date DATE,
  last_seen DATE,
  date_of_birth DATE,
  phone_number VARCHAR(11),
  city VARCHAR(50),
  state VARCHAR(50),
  country VARCHAR(50)
);




# Tags Table
CREATE TABLE IF NOT EXISTS tags
(
  tag_id INT PRIMARY KEY,
  tag_name VARCHAR(255) NOT NULL,
  INDEX idx_tag_name (tag_name)
);


# Media Table
CREATE TABLE IF NOT EXISTS media (
   media_id INT PRIMARY KEY
);


# Media Images Table
CREATE TABLE IF NOT EXISTS media_images (
  id INT PRIMARY KEY,
  image_type VARCHAR(50),
  image_link VARCHAR(255),
  photographer VARCHAR(255),
  title VARCHAR(50),
  description TEXT(2000),
  resolution VARCHAR(50),
  date_taken DATE,
  file_format VARCHAR(20),
  CONSTRAINT fk_media_images
      FOREIGN KEY (id) REFERENCES media(media_id)
      ON UPDATE CASCADE ON DELETE CASCADE
);


# Media literature table title, publisher, publication_date, genre, page_count, budget, ISBN

CREATE TABLE IF NOT EXISTS media_literature
(
  id INT PRIMARY KEY,
  description TEXT(2000),
  author VARCHAR(255),
  link VARCHAR(255),
  type VARCHAR(50),
  title VARCHAR(50),
  publisher VARCHAR(50),
  publication_date DATE,
  genre VARCHAR(50),
  page_count INTEGER,
  budget DECIMAL(10,2),
  ISBN VARCHAR(13),

  CONSTRAINT fk_media_literature
      FOREIGN KEY (id) REFERENCES media(media_id)
      ON UPDATE CASCADE ON DELETE CASCADE
);




# Media videos table
CREATE TABLE IF NOT EXISTS media_videos
(
  id INT PRIMARY KEY,
  length INT,
  description TEXT(2000),
  video_type VARCHAR(50),
  name TEXT,
  size BIGINT,   #size in bytes
  quality VARCHAR(20),
  genre VARCHAR(50),
  director VARCHAR(50),
  CONSTRAINT fk_media_videos
      FOREIGN KEY (id) REFERENCES media(media_id)
    ON UPDATE CASCADE ON DELETE CASCADE
);




# Media_tags relationship table
CREATE TABLE IF NOT EXISTS media_tags
(
  media_id INT NOT NULL,
  tag_id INT NOT NULL,


  PRIMARY KEY (media_id, tag_id),
  CONSTRAINT fk_media_tags_media
      FOREIGN KEY (media_id) REFERENCES media(media_id)
          ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_media_tags_tag
      FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
     ON UPDATE CASCADE ON DELETE CASCADE
  );




# user_media subscriptions table
CREATE TABLE IF NOT EXISTS user_media (
  user_id INT NOT NULL,
  media_id INT NOT NULL,

  PRIMARY KEY (user_id, media_id),
  CONSTRAINT fk_user_media_subscriptions_user
  FOREIGN KEY (user_id) REFERENCES users(user_id)
  ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_user_media_subscriptions_media
  FOREIGN KEY (media_id) REFERENCES media(media_id)
     ON UPDATE CASCADE ON DELETE CASCADE
  );


# Insert Statements
INSERT INTO users (user_id, name, email, profile_bio, phone_number, city, state, country)
VALUES (1, 'John Doe', 'j@gmail.com', 'book enjoyer', 1234567890, 'Boston', 'MA', 'USA'),
(2, 'Bob Myers', 'b@gmail.com', 'movie enjoyer', 5678901234, 'Arlington', 'MA', 'USA'),
(3, 'Ron Washington', 'r@gmail.com', 'picture enjoyer', 9012345678, 'Medford', 'MA', 'USA'),
(4, 'Rahul Shah', 'rs@gmail.com', 'journalist', 9012345679, 'Canton', 'MA', 'USA'),
(5, 'Sara Smith', 'ss@gmail.com', 'movie enjoyer', 8882345679, 'Dallas', 'TX', 'USA'),
(6, 'Barbara Brown', 'barbara@gmail.com', 'book enjoyer', 9992345679, 'Seattle', 'WA', 'USA');




INSERT INTO media (media_id)
VALUES (1),(2),(3),(4),(5),(6),(7);

INSERT INTO media_videos (id, description, video_type, name, quality, genre, director)
VALUES (1, 'second batman movie', 'Movie', 'The Dark Knight Rises', 'HD', 'Action', 'Nolan'),
               (2, 'mafia show', 'Show', 'Sopranos', 'HD','Drama','Chase');

INSERT INTO media_literature (id, description, author, title, genre, page_count)
VALUES (3, 'The second one', 'Rowling', 'The Chamber of Secrets', 'Fantasy', 231),
      (4, 'The sixth one', 'Rowling', 'The half-blood prince', 'Fantasy', 451),
   (5, 'The seventh one', 'Rowling', 'The deathly hallows', 'Fantasy', 751);

INSERT INTO media_images(id, image_type, photographer, title, resolution, file_format)
VALUES (6, 'Nature', 'Doe', 'Lilies in Bloom', '1080x720', 'png'),
   (7, 'Selfie', 'Moe', 'Pic on the Tower', '1080x720', 'jpg');

INSERT INTO tags (tag_id, tag_name)
VALUES (1, 'Mafia'), (2, 'Magic'), (3, 'Masterpiece');

INSERT INTO media_tags (media_id, tag_id)
VALUES (2, 1), (3, 2), (7, 3);

INSERT INTO user_media (media_id, user_id)
VALUES (2, 1), (3, 2), (7, 2);



