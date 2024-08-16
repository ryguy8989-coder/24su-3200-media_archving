import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Initialize sidebar links
SideBarLinks()

# Page title
st.write("# Update a Tag")
st.write("Current Tags:")
# Function to fetch and display existing tags
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
tags = fetch_and_display_tags()

# Section for updating a tag
st.write("## Update a Tag")

# Dropdown to select the old tag name
if tags:
    old_tag_name = st.selectbox("Select a Tag to Update:", [tag['tag_name'] for tag in tags])

    # Text input for the new tag name
    new_tag_name = st.text_input("Enter New Tag Name:")

    if st.button("Update Tag"):
        if not new_tag_name:
            st.error("New tag name cannot be empty.")
        else:
            try:
                # JSON data to be sent in the PUT request
                data = {
                    "old_tag_name": old_tag_name,
                    "new_tag_name": new_tag_name
                }

                # Make a PUT request to update the tag
                response = requests.put('http://api:4000/t/tags', json=data)
                
                if response.status_code == 200:
                    st.success(f"Tag '{old_tag_name}' has been successfully updated to '{new_tag_name}'!")
                    st.write("Current Tags:")
                    tags = fetch_and_display_tags()
                elif response.status_code == 404:
                    st.error(f"Tag '{old_tag_name}' not found.")
                else:
                    st.error(f"Failed to update tag. Server responded with status code {response.status_code}.")
            except Exception as e:
                st.error(f"An error occurred while updating the tag: {str(e)}")
