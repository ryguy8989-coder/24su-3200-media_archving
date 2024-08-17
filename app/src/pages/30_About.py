import streamlit as st
#from streamlit_extras.app_logo import add_logo
#from streamlit_extras.app_media import add_media
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    The Media Archive application has the goal of providing a
      centralized location for the organization of various types of media, 
      including books, movies, articles, and images, and other media literature. 
      A lot of similar services are either too disparate in media typing or optimally 
      organized and this app intends to solve that. Its intended users would be the likes
    of avid movie watchers, classical book readers, analysts in media companies, journalists, 
    and content curators. The app will allow a great deal of customization and optimization for 
    the user to decide how to organize their media. This will include a crowdsourced method of 
    media tagging that will allow better descriptions.

    """
        )
