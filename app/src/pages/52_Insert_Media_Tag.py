import streamlit as st
import requests

st.write("# Add a Tag to a Piece of Media")
st.write("Current Images:")
def fetch_and_display_image():
    try:
        images = requests.get('http://api:4000/i/images').json()
        st.dataframe(images)
    except Exception as e:
        st.write(f"Could not connect to the database to get images: {str(e)}")

fetch_and_display_image()

st.write("Current Literature:")
def fetch_and_display_lit():
    try:
        lit = requests.get('http://api:4000/l/lit').json()
        st.dataframe(lit)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get literature: {str(e)}")

fetch_and_display_lit()

st.write("Current Videos:")
def fetch_and_display_video():
    try:
        videos = requests.get('http://api:4000/v/videos').json()
        st.dataframe(videos)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get videos: {str(e)}")

fetch_and_display_video()

st.write("Current Tags:")
def fetch_and_display_tags():
    try:
        # Fetch existing tags from the API
        tags = requests.get('http://api:4000/t/tags').json()
        st.dataframe(tags)
        return tags
    except Exception as e:
        st.write(f"Could not connect to the database to get tags: {str(e)}")
        return []

# Fetch and display tags
fetch_and_display_tags()



st.write("# Add a Piece of Media to Your List")

with st.form("Add Media"):
    tag_id = st.number_input("Tag ID (Integer):", min_value=1, step=1, help="Your user ID.")
    media_id = st.number_input("Media ID (Integer):", min_value=1, step=1, help="The ID of the media you want to add.")

    submitted = st.form_submit_button("Submit")


    if submitted:
        
        data = {
            "tag_id": tag_id,
            "media_id": media_id
        }

        # Send a POST request to the Flask API
        response = requests.post('http://api:4000/m/add_media_tag', json=data)

        if response.status_code == 201:
            st.success("Media added to your list successfully!")
        else:
            st.error(f"Failed to add tag to media. Server responded with status code {response.status_code}.") 
