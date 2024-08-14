import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Accessing a REST API from Within Streamlit")

st.write("Test")
#media_ids = requests.get('http://api:4000/mids/media_ids').json()
#try:
#  st.dataframe(media_ids)
#except:
#  st.write("Could not connect to database to get media ids")


users = requests.get('http://api:4000/u/users').json()
try:
  st.dataframe(users)
except:
  st.write("Could not connect to database to get users")

#If you want to run this, change DB_name in .env
#products = requests.get('http://api:4000/p/products').json()
#try:
#  st.dataframe(products)
#except:
#  st.write("Could not connect to database to get products")

"""
Simply retrieving data from a REST api running in a separate Docker Container.

If the container isn't running, this will be very unhappy.  But the Streamlit app 
should not totally die. 
"""
'''

data = {} 
try:
  data = requests.get('http://api:4000/data').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)
'''