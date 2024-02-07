# Import necessary libraries
from dotenv import load_dotenv  # For loading environment variables from .env file
import os  # For interacting with the operating system
import streamlit as st  # For creating web-based applications
import pandas as pd  # For data manipulation and analysis

# Importing required modules from pandasai library
from pandasai import SmartDataframe  # For enhancing Pandas DataFrame functionality
from pandasai.llm.openai import OpenAI  # For using OpenAI language models

# Load environment variables from .env file (e.g., OPEN_AI_API_KEY)
load_dotenv()

# Get the OpenAI API key from the environment variables
API_KEY = os.environ['OPEN_AI_API_KEY']
print(API_KEY)  # Print the API key (for debugging purposes)

# Create an instance of the OpenAI language model using the API key
llm = OpenAI(api_token=API_KEY)

# Create a SmartDataframe object, which enhances Pandas DataFrame with AI capabilities
pandasai = SmartDataframe(llm)

# Set the title for the Streamlit web application
st.title("🐼 Prompt driven analysis with Pandas AI")

# Allow users to upload a CSV file for analysis
uploaded_file = st.file_uploader("💬 Upload CSV file for analysis", type=['csv'])

# If a file is uploaded
if uploaded_file is not None:
    # Read the uploaded CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the first 3 rows of the DataFrame
    st.write(df.head(3))
    
    # Provide a text area for users to enter their analysis prompt
    prompt = st.text_area("Enter your prompt")
    
    # If the "Generate" button is clicked
    if st.button("Generate"):
        # If a prompt is provided
        if prompt:
            # Indicate that Pandas AI is generating an answer
            st.write("Pandas AI is generating an answer..")
            
            # Generate an AI-driven analysis based on the prompt and display the result
            st.write(pandasai.run(df, prompt=prompt))
        else:
            # Display a warning message if no prompt is provided
            st.warning("Please enter a prompt")
