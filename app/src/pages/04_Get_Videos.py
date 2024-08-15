import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Here is all the Videos in Our Database")

st.write("All Videos")

videos = requests.get('http://api:4000/v/videos').json()
try:
  st.dataframe(videos)
except:
  st.write("Could not connect to database to get videos")
