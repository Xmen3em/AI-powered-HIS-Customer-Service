import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Hospital RAG System", page_icon="🏥", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        .big-font { font-size:24px !important; font-weight: bold; }
        .medium-font { font-size:18px !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<p class='big-font'>Hospital RAG System</p>", unsafe_allow_html=True)
st.markdown("<p class='medium-font'>Ask any question about hospital services and policies.</p>", unsafe_allow_html=True)

# User Input
query = st.text_input("Enter your query:")

# Submit Button
if st.button("Submit", use_container_width=True):
    with st.spinner("Fetching response..."):
        response = requests.post("http://localhost:8000/ask", json={"query": query})
        if response.status_code == 200:
            st.success("Response received successfully!")
            st.write(response.json()["answer"])
        else:
            st.error("Failed to get a response. Please try again.")
