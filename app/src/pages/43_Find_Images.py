import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Initialize sidebar links
SideBarLinks()

# Page title
st.write("# Searching Media Images by Tag")

# Function to fetch and display existing tags
def fetch_and_display_tags():
    try:
        # Make a GET request to fetch tags from the API
        tags = requests.get('http://api:4000/t/tags').json()
        # Display the tags in a dataframe
        st.dataframe(tags)
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get tags: {str(e)}")

# Call the function to fetch and display tags
fetch_and_display_tags()

# Section for finding images by tag
st.write("## Find Images by Tag")

with st.form("Find Images"):
    search_tag = st.text_input("Input Tag to Search Images:")  # Text input for the tag to search
    search_submitted = st.form_submit_button("Search")  # Submit button for searching images

    if search_submitted:
        try:
            # Make a GET request to find images by tag
            response = requests.get(f'http://api:4000/images?tag={search_tag}')

            # Check if the response is empty or not JSON
            if response.status_code == 200 and response.content:
                try:
                    images = response.json()  # Attempt to parse JSON response

                    if images:
                        # Display the found images in a dataframe
                        st.dataframe(images)
                    else:
                        st.write(f"No images found for tag '{search_tag}'.")
                except ValueError:
                    st.error("Failed to parse the response. The server may not have returned valid JSON.")
            else:
                st.write(f"No images found for tag '{search_tag}'.")
        except Exception as e:
            st.error(f"An error occurred while searching for images: {str(e)}")

