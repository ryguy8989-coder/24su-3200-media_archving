import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
#from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Creating a New Tag")
st.write("Current Tags:")

def fetch_and_display_tags():
    try:
        tags = requests.get('http://api:4000/t/tags').json()
        st.dataframe(tags)
    except:
        st.write("Could not connect to the database to get tags")

fetch_and_display_tags()

with st.form("Create a New Tag"):
    tag_name = st.text_input("Input New Tag:")

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {}
        data['tag_name'] = tag_name
        # st.write(data)
        requests.post('http://api:4000/t/tags', json=data)
        response = requests.post('http://api:4000/t/tags', json=data)
        st.success(f"Tag '{tag_name}' has been successfully created!")
        


