import streamlit as st

def read_text_file(uploaded_file):
    content = uploaded_file.getvalue().decode("utf-8")
    return content

def chatbot(question, text_content):
    responses = {
        "What is in the file?": text_content,
        "How many lines are in the file?": f"The file contains {len(text_content.splitlines())} lines.",
        # Add more predefined responses here
    }
    return responses.get(question, "I'm sorry, I don't understand that question.")

# Streamlit UI
st.title("Text File Chatbot")

uploaded_file = st.file_uploader("Upload text file", type=['txt'])

if uploaded_file is not None:
    text_content = read_text_file(uploaded_file)
    st.write("Text content:")
    st.write(text_content)

    question = st.text_input("Ask a question")
    if st.button("Ask"):
        if question:
            response = chatbot(question, text_content)
            st.write("Chatbot's response:")
            st.write(response)
        else:
            st.warning("Please enter a question.")
