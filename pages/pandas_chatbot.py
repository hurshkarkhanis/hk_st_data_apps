import pandas as pd
import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get api key from .env file
api_key = os.getenv("OPEN_AI_API_KEY")

# Ensure the API key is passed correctly
if api_key is None:
    st.error("API key is missing. Please provide the API key in the .env file.")
    st.stop()

llm = OpenAI(temperature=0.9, api_token=api_key)

st.title("🐼 Pandas AI: Query CSV in natural language (in progress)")
uploaded_file = st.file_uploader("💬 Upload file for analysis", type=['csv'])


if uploaded_file is not None:
    # Read the uploaded file into a Pandas DataFrame
    pandas = pd.read_csv(uploaded_file)
    smart_df = SmartDataframe(pandas, config={"llm": llm})

    with st.expander("See Full Data"):
        st.write(pandas)

    prompt = st.text_area("Enter prompt")

    if st.button("Generate"):
        if prompt:
            # Show spinner while processing
            with st.spinner("Generating..."):
                output = smart_df.chat(prompt)    
            # Hide spinner when done
            st.success("Generated!")
            st.write(output)
        else:
            st.warning("Please enter a prompt")
    
