import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

# Initialize sidebar links
SideBarLinks()

st.write(" ## Top 10 Trending Tags")

try:
    # Make a GET request to find images by tag
    response = requests.get('http://api:4000/t/tags/trending')

    # Check if the response is empty or not JSON
    if response.status_code == 200 and response.content:
        try:
            tags = response.json()  # Attempt to parse JSON response
            if tags:
                # Display the found images in a dataframe
                st.dataframe(tags)
            else:
                st.write('No Tags found')
        except ValueError:
            st.error("Failed to parse the response. The server may not have returned valid JSON.")
    else:
        st.write('No Tags found')
except Exception as e:
    st.error(f"An error occurred while searching for tags: {str(e)}")
