import streamlit as st
import pandas as pd

import random as rand

# Sample DataFrame (Replace this with your actual dataset)
# Sample DataFrame with consistent lengths


data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-27', freq='D'),
    'Descrip': ["hursh" for _ in range(1, 28)],
    'Category': ['Investing', 'Housing', 'Gym'] * 9,  # Adjust the length of Category
    'Amount': [rand.randint(1, 100) for _ in range(27)],
    'Notes': ["hursh" for _ in range(1, 28)]
}

df = pd.DataFrame(data)





df = pd.DataFrame(data)

# Sidebar filters

st.header('Filters')

start_date = st.date_input("Start Date", min_value=df['Date'].min().date(), max_value=df['Date'].max().date(), value=df['Date'].min().date())
end_date = st.date_input("End Date", min_value=df['Date'].min().date(), max_value=df['Date'].max().date(), value=df['Date'].max().date())
selected_categories = st.multiselect('Select Categories', df['Category'].unique())

# Apply filters
filtered_df = df[(df['Date'] >= pd.Timestamp(start_date)) & (df['Date'] <= pd.Timestamp(end_date))]
if selected_categories:
    filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]

# Data
with st.expander("See Full Data"):
        st.write(filtered_df)


# Chart
st.header('Chart')
if not filtered_df.empty:
    filtered_chart_data = filtered_df.groupby('Date')['Amount'].sum()
    st.bar_chart(filtered_chart_data)
else:
    st.write('No data available for the selected filters.')