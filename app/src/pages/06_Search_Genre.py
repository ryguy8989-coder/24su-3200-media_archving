import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()


with st.form("Find Videos by Genre"):
    st.write("## Find Videos based on Genre")
    search_genre = st.text_input("Input Video Genre:")

    submitted = st.form_submit_button("Search")

    if submitted:
        try: # Make a GET request to find videos by genre
            results = requests.get(f'http://api:4000/v/videos/{search_genre}')

            if results.status_code == 200:
                videos = results.json() # Attempt to parse JSON response

                if videos:
                    # Display found videos in dataframe
                    st.dataframe(videos)
                else:
                    st.write(f"No videos found in the '{search_genre}' genre.")
            else:
                st.write(f"No videos found for genre '{search_genre}'. Status code: {results.status_code}")
        except requests.RequestException as e:
            st.error(f"An error occured while searching for videos: {str(e)}")