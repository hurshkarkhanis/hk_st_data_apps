import streamlit as st
import pandas as pd
import json

def flatten_json(json_data, parent_key='', separator='_'):
    """
    Flatten JSON data with nested structures.
    """
    items = {}
    for key, value in json_data.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, separator))
        elif isinstance(value, list):
            for i, v in enumerate(value):
                new_key = new_key + separator + str(i)
                if isinstance(v, dict):
                    items.update(flatten_json(v, new_key, separator))
                else:
                    items[new_key] = v
        else:
            items[new_key] = value
    return items

def json_to_dataframe(json_data):
    """
    Convert JSON data to Pandas DataFrame.
    """
    flat_data = flatten_json(json_data)
    return pd.DataFrame([flat_data])

def main():
    st.title('JSON File to Pandas DataFrame')

    # File upload
    st.header('Upload JSON File')
    uploaded_file = st.file_uploader("Choose a JSON file", type=['json'])

    if uploaded_file is not None:
        try:
            # Read JSON file
            json_data = json.load(uploaded_file)
            df = json_to_dataframe(json_data)

            # Display DataFrame
            st.header('Pandas DataFrame')
            st.write(df)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
