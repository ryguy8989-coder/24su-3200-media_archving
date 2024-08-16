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

if st.button('Add Media to List', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/51_Insert_User_Media.py')

if st.button('Add Tag to Media', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/52_Insert_Media_Tag.py')

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

if st.button('Find Top 10 Tags',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Trending_Tags.py')
  
if st.button('Update Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Update_Tag.py')

if st.button('Delete Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Delete_Tag.py')


if st.button('Insert New Video', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Insert_New_Video.py')


if st.button('Insert New Literature', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/26_Insert_New_Literature.py')

if st.button('Insert New Image', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/27_Insert_New_Image.py')


 