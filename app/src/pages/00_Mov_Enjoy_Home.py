import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Movie Enjoyer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

#if st.button('View World Bank Data Visualization', 
 #            type='primary',
  #           use_container_width=True):
  #st.switch_page('pages/01_World_Bank_Viz.py')

#if st.button('View World Map Demo', 
 #            type='primary',
  #           use_container_width=True):
 # st.switch_page('pages/02_Map_Demo.py')

if st.button('See all Videos', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Get_Videos.py')

if st.button('Add Tag to Media', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/52_Insert_Media_Tag.py')

if st.button('Add Media to List', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/51_Insert_User_Media.py')

if st.button("Create a New Tag",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Create_New_Tag.py')

if st.button('Find Videos Based On Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Find_Videos.py')

if st.button('Find Videos Based On Genre', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/06_Search_Genre.py')

if st.button('Update Tag', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Update_Tag.py')

