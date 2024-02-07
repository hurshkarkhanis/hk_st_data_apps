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


import requests

def get_flight_data():
    url = "https://opensky-network.org/api/states/all"
    params = {
    "lamin": 40.4774,  # Minimum latitude for NYC
    "lamax": 40.9176,  # Maximum latitude for NYC
    "lomin": -74.2591, # Minimum longitude for NYC
    "lomax": -73.7002  # Maximum longitude for NYC
}


    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["states"]  # Extract the flight data from the response
        else:
            print("Error: Unable to fetch flight data (HTTP Status Code:", response.status_code, ")")
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

# Example usage:
flight_data = get_flight_data()
if flight_data:
    print("Number of flights tracked:", len(flight_data))
    for flight in flight_data:
        print("Flight:", flight[0], "Callsign:", flight[1], "Longitude:", flight[5], "Latitude:", flight[6])

