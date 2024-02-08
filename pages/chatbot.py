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

llm = OpenAI(api_token=api_key)

st.title("🐼 Pandas AI: Prompt driven analysis")
uploaded_file = st.file_uploader("💬 Upload file for analysis", type=['csv', 'xlsx', 'json','sql'])




def read_file(input_file):
    if input_file.name.endswith('.csv'):
        return pd.read_csv(input_file)
    elif input_file.name.endswith('.xlsx'):
        return pd.read_excel(input_file, engine='openpyxl')
    elif input_file.name.endswith('.json'):
        return pd.read_json(input_file)
    elif input_file.name.endswith('.sql'):
        # Example for reading from SQL database
        # return pd.read_sql_query("SELECT * FROM table_name", connection)
        pass
    else:
        raise ValueError("Unsupported file format")


if uploaded_file is not None:
    try:
        # Read the uploaded file into a Pandas DataFrame
        pandas = read_file(uploaded_file)
        smart_df = SmartDataframe(pandas, config={"llm": llm})

        with st.expander("See Full Data"):
            st.write(pandas)

        prompt_num = 1
        prompts_outputs = []  # List to store prompts and their corresponding outputs

        while True:
            prompt = st.text_area(f"Enter prompt #{prompt_num}")

            # Display previous prompts and outputs
            for i, (prev_prompt, output) in enumerate(prompts_outputs):
                st.write(f"Input {i+1}: {prev_prompt}")
                st.write(f"Output {i+1}: {output}")

            button_key = f"generate_button_{prompt_num}"  # Unique key for each button
            if st.button("Generate", key=button_key):
                if prompt:
                    # Show spinner while processing
                    with st.spinner("Generating..."):
                        output = smart_df.chat(prompt)
                        prompts_outputs.append((prompt, output))
                    # Hide spinner when done
                    st.success("Generated!")
                    prompt_num += 1
                else:
                    st.warning("Please enter a prompt")
            else:
                break
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
