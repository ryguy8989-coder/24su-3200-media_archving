import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Book Enjoyer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View all Literature', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_View_Literature.py')

if st.button("Create a New Tag",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Create_New_Tag.py')

if st.button("Find Literature Based on Tag",
            type='primary',
            use_container_width=True):
 st.switch_page('pages/13_Find_Literature.py')
 
if st.button('Update Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Update_Tag.py')