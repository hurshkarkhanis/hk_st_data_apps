import pandas as pd
from langchain.llms import OpenAI
import streamlit as st

from dotenv import load_dotenv
import os

st.title('🦜🔗 LangChain Chatbot (in progress)')

st.caption("using Langchain to create text based chatbot")

load_dotenv()
openai_api_key = os.getenv("OPEN_AI_API_KEY")

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
