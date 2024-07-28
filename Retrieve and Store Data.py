import streamlit as st
import pandas as pd
import googleapiclient.discovery
from sqlalchemy 
import create_engine
# Function to extract relevant data
def extract_data(data):
    channel_info = data['items'][0]
    channel_data = {
        "Channel_Name": channel_info['snippet']['title'],
        "Channel_Id": channel_info['id'],
        "Subscription_Count": channel_info['statistics']['subscriberCount'],
        "Total_Views": channel_info['statistics']['viewCount'],
        "Total_Videos": channel_info['statistics']['videoCount'],
        "Playlist_Id": channel_info['contentDetails']['relatedPlaylists']['uploads']
    }
    return channel_data

# Function to store data in MySQL or PostgreSQL
def store_data(data, db_choice):
    df = pd.DataFrame([data])
    if db_choice == "MySQL":
        engine = create_engine('mysql+pymysql://root:password@localhost/youtube')
    elif db_choice == "PostgreSQL":
        engine = create_engine('postgresql+psycopg2://username:password@localhost/youtube')
    df.to_sql('channels', con=engine, if_exists='append', index=False)

# Options to choose SQL database
db_choice = st.selectbox("Choose SQL Database:", ["MySQL", "PostgreSQL"])

if st.button("Store Channel Data"):
    if api_key and channel_id and db_choice:
        data = get_channel_data(api_key, channel_id)
        channel_data = extract_data(data)
        store_data(channel_data, db_choice)
        st.success("Data stored successfully in {}".format(db_choice))
    else:
        st.error("Please provide API key, Channel ID, and select a database")
