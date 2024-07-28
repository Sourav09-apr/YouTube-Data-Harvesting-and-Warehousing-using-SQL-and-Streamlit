import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import googleapiclient.discovery
from sqlalchemy import create_engine
def plot_data(df, x, y, plot_type="bar"):
    fig, ax = plt.subplots()
    if plot_type == "bar":
        df.plot(kind='bar', x=x, y=y, ax=ax)
    elif plot_type == "line":
        df.plot(kind='line', x=x, y=y, ax=ax)
    st.pyplot(fig)

if st.button("Plot Data"):
    if db_choice:
        result = retrieve_data(query_choice, db_choice)
        plot_data(result, 'Channel_Name', 'Subscription_Count')
    else:
        st.error("Please select a database")

