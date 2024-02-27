import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from pandasql import sqldf

import pandasql as ps

st.title("📗 Mint")

url = "https://docs.google.com/spreadsheets/d/1n-hcvcfR4yMxqcolyOq2rBauGH1nFtCkWYYZgUgyEDs/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from Google Sheets
google_data = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3])

st.title("Google Sheet")
st.write(google_data)

pandas_data = pd.DataFrame(google_data)

st.title("PandasDF")

st.write(pandas_data)

#====================

st.title("asking user to filter")

start_date = st.date_input("Select start date")
end_date = st.date_input("Select end date")

# Convert selected dates to the format in DataFrame
start_date_str = start_date.strftime("%m/%d/%y")
end_date_str = end_date.strftime("%m/%d/%y")

print(start_date, type(start_date))
print(end_date, type(end_date))

print("-----")


print(start_date_str, type(start_date_str))

print(end_date_str, type(end_date_str))


# Filter dates between the time frame

filtered_df = pandas_data[pandas_data['Date'] > '1/7/24']

st.title("Filtered")

st.write(filtered_df)



