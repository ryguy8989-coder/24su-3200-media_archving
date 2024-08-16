import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Here is all the Literature in Our Database")

st.write("All Literature")

lit = requests.get('http://api:4000/l/lit').json()
try:
  st.dataframe(lit)
except:
  st.write("Could not connect to database to get literature")
