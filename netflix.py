import streamlit as st
import pandas as pd
import googleapiclient.discovery
import sqlalchemy
from sqlalchemy import create_engine

# Initialize Streamlit
st.title("YouTube Data Harvesting and Warehousing")

# Input YouTube API Key and Channel ID
api_key = st.text_input("Enter your YouTube API Key:")
channel_id = st.text_input("Enter YouTube Channel ID:")

# Function to retrieve data from YouTube API
def get_channel_data(api_key, channel_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
    response = request.execute()
    return response

# Display channel data
if st.button("Fetch Channel Data"):
    if api_key and channel_id:
        data = get_channel_data(api_key, channel_id)
        st.json(data)
    else:
        st.error("Please provide both API key and Channel ID")

