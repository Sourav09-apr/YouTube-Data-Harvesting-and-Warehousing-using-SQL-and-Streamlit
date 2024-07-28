import streamlit as st
import pandas as pd
import googleapiclient.discovery
from sqlalchemy import create_engine

# Function to retrieve data from SQL database
def retrieve_data(query, db_choice):
    if db_choice == "MySQL":
        engine = create_engine('mysql+pymysql://username:password@localhost/youtube')
    elif db_choice == "PostgreSQL":
        engine = create_engine('postgresql+psycopg2://username:password@localhost/youtube')
    df = pd.read_sql(query, con=engine)
    return df

# Query examples
queries = [
    "SELECT * FROM channels",
    "SELECT Channel_Name, COUNT(*) as Video_Count FROM videos GROUP BY Channel_Name ORDER BY Video_Count DESC",
   
]

query_choice = st.selectbox("Choose a query to execute:", queries)

if st.button("Execute Query"):
    if db_choice:
        result = retrieve_data(query_choice, db_choice)
        st.dataframe(result)
    else:
        st.error("Please select a database")
