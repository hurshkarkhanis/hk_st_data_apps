import pandas as pd
from pandasai import SmartDataframe
import streamlit as st

# Instantiate a LLM
from pandasai.llm import OpenAI
llm = OpenAI(api_token='OPEN_AI_API_KEY')

st.title("🐼 Pandas AI: Prompt driven analysis")

# Allow users to upload a CSV file for analysis
uploaded_file = st.file_uploader("💬 Upload CSV file for analysis", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Read the uploaded CSV file into a Pandas DataFrame
    pandas_df = pd.read_csv(uploaded_file)
    smart_df = SmartDataframe(pandas_df, config={"llm": llm})
    st.write(pandas_df.head(3))
    prompt = st.text_area("Enter prompt #1")
    num_prompts = 1


    if st.button("Generate"):
        if prompt:
            st.write("Pandas AI is generating an answer")
            output = smart_df.chat(prompt)
            st.write(output)
            prompt = st.text_area("Enter prompt #" + str(num_prompts))
            num_prompts += 1
        else:
            st.warning("Please enter a prompt")
