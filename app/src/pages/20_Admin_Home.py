import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

if st.button('Update ML Models', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_ML_Model_Mgmt.py')

if st.button('Get All Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Get_Users.py')
  
if st.button("Create a New Tag",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Create_New_Tag.py')