import streamlit as st
import requests

st.write("# Add a New Media Image")

# Form to input image details
with st.form("Add Image"):
    id = st.number_input("Image ID (Integer):", min_value=1, step=1, help="Unique identifier for the image.")
    image_type = st.text_input("Image Type", help="E.g., landscape, portrait, abstract")
    image_link = st.text_input("Image Link", help="URL of the image")
    photographer = st.text_input("Photographer", help="Name of the photographer")
    title = st.text_input("Title", help="Title of the image")
    description = st.text_area("Description", help="Description of the image")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Prepare the data to send
        data = {
            "id": id,
            "image_type": image_type,
            "image_link": image_link,
            "photographer": photographer,
            "title": title,
            "description": description
        }

        # Send a POST request to the Flask API
        response = requests.post('http://api:4000/i/images', json=data)
        
        if response.status_code == 201:
            st.success("Media image added successfully!")
        elif response.status_code == 400:
            st.error("Missing required fields. Please fill in all fields.")
        else:
            st.error(f"Failed to add image. Server responded with status code {response.status_code}.")
