import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import altair as alt


st.title("📊 Dashboards (in progress)")
st.caption("Connecting to Google Sheets and/or requestds APIs to vizualize live data")

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
        "lamin": 24.396308,   # Lower latitude bound for Florida
        "lamax": 31.001056,   # Upper latitude bound for Florida
        "lomin": -87.634819,  # Lower longitude bound for Florida
        "lomax": -79.974307   # Upper longitude bound for Florida
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

longs = []
lats = []

flight_data = get_flight_data()
if flight_data:
    print("Number of flights tracked:", len(flight_data))
    for flight in flight_data:
        print("Flight:", flight[0], 
              "Callsign:", flight[1], 
              "Longitude:", flight[5], 
              "Latitude:", flight[6])
        longs.append(flight[5])
        lats.append(flight[6])


print("Number of flights tracked:", len(flight_data))

st.metric("Number of Flights", len(flight_data))


d = {'longitude': longs, 'latitude': lats}
df = pd.DataFrame(data=d)

st.map(df, color ="#EE4B2B", size=40)




