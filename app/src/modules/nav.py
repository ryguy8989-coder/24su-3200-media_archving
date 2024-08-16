# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Examples for Role of Movie Enjoyer ------------------------
def MovEnjoyHomeNav():
    st.sidebar.page_link("pages/00_Mov_Enjoy_Home.py", label="Movie Enjoyer Home", icon='👤')

#def WorldBankVizNav():
#    st.sidebar.page_link("pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon='🏦')

def SearchWithGenreNav():
    st.sidebar.page_link("pages/06_Search_Genre.py", label="Find Videos with Genre", icon='🗺️')

def GetVideos():
    st.sidebar.page_link("pages/04_Get_Videos.py", label="Get Videos", icon='🗺️')

## ------------------------ Examples for Role of Book Enjoyer ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')

def NewTagNav():
    st.sidebar.page_link("pages/14_Create_New_Tag.py",label="Add a New Tag", icon='🖥️')

#def PredictionNav():
#    st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

def FindLiteratureWithGenreNav():
    st.sidebar.page_link("pages/13_Find_Literature.py", label="Find Literature with Genre", icon='🖥️')

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/43_Find_Images.py", label='Find Images by tag', icon='🏢')
    st.sidebar.page_link("pages/22_Get_Users.py", label='Get all Users', icon='🏢')
    st.sidebar.page_link("pages/23_Trending_Tags.py", label='Get Trending Tags', icon='🏢')
#### ------------------------ System Admin Role ------------------------
def JournalistPageNav():
    st.sidebar.page_link("pages/40_Journalist_Home.py", label="Journalist", icon='🖥️')
    st.sidebar.page_link("pages/41_Get_Images.py", label="Get All Images", icon='🖥️')

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'movie_enjoyer':
            MovEnjoyHomeNav()
            #WorldBankVizNav()
            NewTagNav()
            SearchWithGenreNav()

        # If the user role is book enjoyer, show the Api Testing page
        if st.session_state['role'] == 'book_enjoyer':
         #   PredictionNav()
            ApiTestNav() 
            NewTagNav()
            FindLiteratureWithGenreNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'administrator':
            AdminPageNav()
            NewTagNav()
        
        # If the user is an journalist, give them access to the journalist pages
        if st.session_state['role'] == 'journalist':
            JournalistPageNav()
            NewTagNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

