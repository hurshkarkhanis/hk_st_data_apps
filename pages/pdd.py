import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import altair as alt

# Define the Google Sheets URL
url = "https://docs.google.com/spreadsheets/d/1vW1qzYSqPyWxZAyraNM83V8AzPotnOlfXT35ZbvfnfE/edit?usp=sharing"

# Establish connection to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from Google Sheets
data = conn.read(spreadsheet=url, usecols=[0, 1])

# Display the raw data
st.write("Raw Data:", data)

# Create a line chart using Altair
chart = alt.Chart(data).mark_line().encode(
    x='Date',
    y=alt.Y('Close').scale(zero=False))


# Display the line chart
st.altair_chart(chart, use_container_width=True)  # Adjust to fit container width
