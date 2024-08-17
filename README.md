# Summer 2024 CS 3200 Project Template Repository

## Project Name: Media Archiving
## Team Members: Ryan Jiang (ryguy8989-coder), Hersh Joshi (hershjoshii), Martin Celo (Cajmali), Moses Yawe (mosyawe1), Santiago Arango(LuchotheCat)



## About

The Media Archive application has the goal of providing a centralized location for the organization of various types of media, including books, movies, articles, and images, and other media literature. A lot of similar services are either too disparate in media typing or optimally organized and this app intends to solve that. Its intended users would be the likes of avid movie watchers, classical book readers, analysts in media companies, journalists, and content curators. The app will allow a great deal of customization and optimization for the user to decide how to organize their media. This will include a crowdsourced method of media tagging that will allow better descriptions.

To achieve our goals of accessible media– books, movies, articles, and images– we organized our data into three main categories: media, videos, and images. Each of these categories all revolve around a common attribute: tags. These tables are as such broken into separate tables, or relations, where there is a certain amount of criteria, its respective attributes, in each of these categories to be met that can identify its value and henceforth make it useful for any users of our app. 


**Relations**

This entity is characterisized by the attributes description, title, genre, ISBN, Page Count, Budget, Publisher, Publication Date, Literature Video Type (book, article, etc), Literature Link for where we can find this piece of writing, and the Author. This relation is mainly characterized by its Media ID, since this category value cannot be repeated for any two different pieces of literature. Similarly, the Media Video relation, and the Media Images relations are also described by their Media_ID attribute. 

Unlike the Mideo Literature relation, the Media Video relation only includes nine attributes: Media ID, Length, Quality, Director, Description, Video Type (Movie, show, etc.), Name, Size, and Genre. This relation is where all the information about finding videos is stored and if a user wants to add another video reference for others to find, they must provide a value that satisfies each of these traits. 

Whenever a particular user frequently references a specific type of visual content, it is often observed that to search for related Media Videos and Images together, as seen with the Jouranlist and Analytics users. This suggests that the formats of these two relations ought to be closely aligned, as the search requirements would need to be similar. As such, like the Mideo Video relation, the Media Images relation includes nine attributes as well: Media ID, Resolution, Image Link, Date Taken, Image Type (jpg, png, hrec, etc), Photographer, Title, File Format, and the Description. In this table as well, if a Value is to be added to this table, it would need to have a sub-value for each of the attributes for this table.

Two more smaller components to this app include the Users and Tags. The Users relation on this app only consists of the User ID and Media ID, both of which contain values that uniquely identify each row in a table. With this table the amount of users can be changed as per needed. These users then have power to create, delete of modify the tags in this app. This tags table is characterized by TagID and the TagName, where the uniquely identifiable column is the TagID. Together, all these components make up this media archieving app.


## Current Project Components


Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## Getting Started for Personal Exploration
1. Clone the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
1. Start the docker containers. 

## Getting Started For Team Project
1. Each team member should make a GitHub account if you don't already have one.  This should be for the public GitHub, not Khoury's enterprise server. 
1. One team member should fork this repository. They will be the repo owner. 
1. Add your team members as Collaborators on the repository.  You can find Collaborators under the Settings tab in the repository.
1. Each team member needs to accept the invitation to collaborate
1. Each team member (including the repo owner) needs to clone the repository to their laptops. 

## Handling User Role Access and Control

In most applications, when a user logs in, they assume a particular role.  For instance, when one logs in to a stock price prediction app, they may be a single investor, a portfolio manager, or a corporate executive (of a publicly traded company).  Each of those *roles* will likely present some similar features as well as some different features when compared to the other roles. So, how do you accomplish this in Streamlit?  This is sometimes called Role-based Access Control, or **RBAC** for short. 

The code in this project demonstrates how to implement a simple RBAC system in Streamlit but without actually using user authentication (usernames and passwords).  The Streamlit pages from the original template repo are split up among 3 roles - Political Strategist, USAID Worker, and a System Administrator role (this is used for any sort of system tasks such as re-training ML model, etc.). It also demonstrates how to deploy an ML model. 

Wrapping your head around this will take a little time and exploration of this code base.  Some highlights are below. 

### Getting Started with the RBAC 
1. We need to turn off the standard panel of links on the left side of the Streamlit app. This is done through the `app/src/.streamlit/config.toml` file.  So check that out. We are turning it off so we can control directly what links are shown. 
1. Then I created a new python module in `app/src/modules/nav.py`.  When you look at the file, you will se that there are functions for basically each page of the application. The `st.sidebar.page_link(...)` adds a single link to the sidebar. We have a separate function for each page so that we can organize the links/pages by role. 
1. Next, check out the `app/src/Home.py` file. Notice that there are 3 buttons added to the page and when one is clicked, it redirects via `st.switch_page(...)` to that Roles Home page in `app/src/pages`.  But before the redirect, I set a few different variables in the Streamlit `session_state` object to track role, first name of the user, and that the user is now authenticated.  
1. Notice near the top of `app/src/Home.py` and all other pages, there is a call to `SideBarLinks(...)` from the `app/src/nav.py` module.  This is the function that will use the role set in `session_state` to determine what links to show the user in the sidebar. 
1. The pages are organized by Role.  Pages that start with a `0` are related to the *Political Strategist* role.  Pages that start with a `1` are related to the *USAID worker* role.  And, pages that start with a `2` are related to The *System Administrator* role. 


## Deploying An ML Model (Totally Optional for CS3200 Project)

*Note*: This project only contains the infrastructure for a hypothetical ML model. 

1. Build, train, and test your ML model in a Jupyter Notebook. 
1. Once you're happy with the model's performance, convert your Jupyter Notebook code for the ML model to a pure python script.  You can include the `training` and `testing` functionality as well as the `prediction` functionality.  You may or may not need to include data cleaning, though. 
1. Check out the  `api/backend/ml_models` module.  In this folder, I've put a sample (read *fake*) ML model in `model01.py`.  The `predict` function will be called by the Flask REST API to perform '*real-time*' prediction based on model parameter values that are stored in the database.  **Important**: you would never want to hard code the model parameter weights directly in the prediction function.  tl;dr - take some time to look over the code in `model01.py`.  
1. The prediction route for the REST API is in `api/backend/customers/customer_routes.py`. Basically, it accepts two URL parameters and passes them to the `prediction` function in the `ml_models` module. The `prediction` route/function packages up the value(s) it receives from the model's `predict` function and send its back to Streamlit as JSON. 
1. Back in streamlit, check out `app/src/pages/11_Prediction.py`.  Here, I create two numeric input fields.  When the button is pressed, it makes a request to the REST API URL `/c/prediction/.../...` function and passes the values from the two inputs as URL parameters.  It gets back the results from the route and displays them. Nothing fancy here.


 
