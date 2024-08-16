import streamlit as st
import requests

st.write("# Add a Piece of Media to Your List")
st.write("Current Images")
def fetch_and_display_image():
    try:
        # Make a GET request to fetch tags from the API
        images = requests.get('http://api:4000/i/images').json()
        # Display the tags in a dataframe
        st.dataframe(images)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get images: {str(e)}")

# Call the function to fetch and display tags
fetch_and_display_image()

st.write("Current Literature")
def fetch_and_display_lit():
    try:
        lit = requests.get('http://api:4000/l/lit').json()
        st.dataframe(lit)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get literature: {str(e)}")

fetch_and_display_lit()

st.write("Current Videos")
def fetch_and_display_video():
    try:
        videos = requests.get('http://api:4000/v/videos').json()
        st.dataframe(videos)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get videos: {str(e)}")

fetch_and_display_video()


with st.form("Add Media"):
    user_id = st.number_input("User ID (Integer):", min_value=1, step=1, help="Your user ID.")
    media_id = st.number_input("Media ID (Integer):", min_value=1, step=1, help="The ID of the media you want to add.")

    submitted = st.form_submit_button("Submit")


    if submitted:
        
        data = {
            "user_id": user_id,
            "media_id": media_id
        }

        # Send a POST request to the Flask API
        response = requests.post('http://api:4000/m/user_media', json=data)

        if response.status_code == 201:
            st.success("Media added to your list successfully!")
        else:
            st.error(f"Failed to add media. Server responded with status code {response.status_code}.") 
