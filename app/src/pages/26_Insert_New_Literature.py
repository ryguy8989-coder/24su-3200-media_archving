import streamlit as st
import requests
from modules.nav import SideBarLinks

# Initialize sidebar links
SideBarLinks()

# Page title
st.write("# Insert a New Literature Entry")

# Form to input literature details
with st.form("Insert New Literature"):
    literature_id = st.number_input("Literature ID (Integer):", min_value=1, step=1, help="Unique identifier for the literature.")
    description = st.text_area("Description:", help="A brief description of the literature.")
    author = st.text_input("Author:", help="Author of the literature.")
    link = st.text_input("Link:", help="Link to the literature (e.g., online article).")
    type = st.text_input("Type (e.g., Book, Article):", help="Type of the literature.")
    title = st.text_input("Title:", help="Title of the literature.")
    publisher = st.text_input("Publisher:", help="Publisher of the literature.")
    publication_date = st.date_input("Publication Date:", help="Date of publication.")
    genre = st.text_input("Genre (e.g., Fiction, Non-Fiction):", help="Genre of the literature.")
    page_count = st.number_input("Page Count (Integer):", min_value=1, step=1, help="Number of pages.")
    budget = st.number_input("Budget (Decimal):", min_value=0.0, format="%.2f", help="Budget for the literature.")
    ISBN = st.text_input("ISBN (13 digits):", help="ISBN number of the literature.")
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Prepare the data to send, filtering out empty fields
        data = {k: v for k, v in {
            "id": literature_id,
            "description": description,
            "author": author,
            "link": link,
            "type": type,
            "title": title,
            "publisher": publisher,
            "publication_date": publication_date.isoformat() if publication_date else None,
            "genre": genre,
            "page_count": page_count if page_count else None,
            "budget": budget if budget else None,
            "ISBN": ISBN
        }.items() if v is not None}

        # Send a POST request to the Flask API
        response = requests.post('http://api:4000/m/literature', json=data)
        
        if response.status_code == 201:
            st.success("Literature entry created successfully!")
        else:
            st.error(f"Failed to create literature entry. Server responded with status code {response.status_code}.")
