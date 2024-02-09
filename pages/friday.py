import pandas as pd

import streamlit as st

uploaded_file = st.file_uploader("💬 Upload file for analysis", type=['json'])

pandas = pd.read_json(uploaded_file, orient='table')


st.write(pandas)