import pandas as pd
from pandasai import SmartDataframe
import streamlit as st

import os
from dotenv import load_dotenv

from pandasai.llm import OpenAI

# Get api key from .env file
api_key = os.getenv("OPEN_AI_API_KEY")

# Ensure the API key is passed correctly
llm = OpenAI(api_token=api_key)

# Load environment variables from .env file
load_dotenv()

st.title("🐼 Pandas AI: Prompt driven analysis")
uploaded_file = st.file_uploader("💬 Upload CSV file for analysis", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Read the uploaded CSV file into a Pandas DataFrame
    pandas_df = pd.read_csv(uploaded_file)
    smart_df = SmartDataframe(pandas_df, config={"llm": llm})

    with st.expander("See Full Data"):
        st.write(pandas_df)

    prompt = st.text_area("Enter prompt")

    if st.button("Generate"):
        if prompt:
            st.write(output)
        else:
            st.warning("Please enter a prompt")









