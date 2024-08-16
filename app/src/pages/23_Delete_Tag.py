import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Initialize sidebar links
SideBarLinks()

# Page title
st.write("# Delete a Tag")

st.write("Current Tags:")
# Function to fetch and display existing tags
def fetch_and_display_tags():
    try:
        # Make a GET request to fetch tags from the API
        tags = requests.get('http://api:4000/t/tags').json()
        # Display the tags in a dataframe
        st.dataframe(tags)
        return tags
    except Exception as e:
        # Handle errors and display a message
        st.write(f"Could not connect to the database to get tags: {str(e)}")
        return []

# Call the function to fetch and display tags
tags = fetch_and_display_tags()

# Section for deleting a tag
st.write("## Delete a Tag")

# List available tags in a dropdown for deletion
if tags:
    tag_to_delete = st.selectbox("Select a Tag to Delete:", [tag['tag_name'] for tag in tags])

    if st.button("Delete Tag"):
        data = {}
        data['tag_name'] = tag_to_delete
        try:
            # Make a DELETE request to delete the selected tag by its name
            requests.delete(f'http://api:4000/t/tags', json=data)
            response = requests.delete(f'http://api:4000/t/tags', json=data)
            
            if response.status_code == 200:
                st.success(f"Tag '{tag_to_delete}' has been successfully deleted!")
            #else:
            #    st.error(f"Failed to delete tag '{tag_to_delete}'. Server responded with status code {response.status_code}.")
        except Exception as e:
            st.error(f"An error occurred while deleting the tag: {str(e)}")
