import streamlit as st
import requests
from modules.nav import SideBarLinks

# Initialize sidebar links
SideBarLinks()

# Page title
st.write("# Insert a New Video")

# Form to input video details
with st.form("Insert New Video"):
    video_id = st.number_input("Video ID (Integer > 200):", min_value=1, step=1, help="Unique identifier for the video.")
    length = st.number_input("Length (Minutes):", min_value=0, step=1, help="Length of the video in minutes.")
    description = st.text_area("Description:", help="A brief description of the video.")
    video_type = st.text_input("Video Type (e.g., Movie, Series):", help="Type of the video.")
    name = st.text_input("Video Name:", help="Name of the video.")
    size = st.number_input("Size (Bytes):", min_value=0, step=1, help="Size of the video file in bytes.")
    quality = st.text_input("Quality (e.g., HD, 4K):", help="Quality of the video.")
    genre = st.text_input("Genre (e.g., Thriller, Comedy):", help="Genre of the video.")
    director = st.text_input("Director:", help="Director of the video.")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Prepare the data to send, filtering out empty fields
        data = {k: v for k, v in {
            "id": video_id,
            "length": length if length else None,
            "description": description,
            "video_type": video_type,
            "name": name,
            "size": size if size else None,
            "quality": quality,
            "genre": genre,
            "director": director
        }.items() if v is not None}

        # Send a POST request to the Flask API
        response = requests.post('http://api:4000/m/videos', json=data)
        
        if response.status_code == 201:
            st.success("Video created successfully!")
        else:
            st.error(f"Failed to create video. Server responded with status code {response.status_code}.")
