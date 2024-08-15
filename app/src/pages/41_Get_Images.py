import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Here is all the Images in Our Database")

st.write("All Images")

images = requests.get('http://api:4000/i/images').json()
try:
  st.dataframe(images)
except:
  st.write("Could not connect to database to get images")