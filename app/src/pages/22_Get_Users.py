import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Here are all the Users in Our Database")

st.write("All Users")

users = requests.get('http://api:4000/u/users').json()
try:
  st.dataframe(users)
except:
  st.write("Could not connect to database to get users")
