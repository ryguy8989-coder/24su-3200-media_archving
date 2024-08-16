import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')


if st.button('Get All Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Get_Users.py')
  
if st.button("Create a New Tag",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Create_New_Tag.py')

if st.button('Find Images Based on Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/43_Find_Images.py')

if st.button("Find Literature Based on Tag",
            type='primary',
            use_container_width=True):
 st.switch_page('pages/13_Find_Literature.py')

if st.button('Find Videos Based On Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Find_Videos.py')

if st.button('Find Trending Tags',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Trending_Tags.py')
 