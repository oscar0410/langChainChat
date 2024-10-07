# Build an LLM app using LangChain with Streamlit

import os
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

# Set page configuration
st.set_page_config(page_title="LLM Chat App", layout="wide")

st.title("Chat with AI")
st.write("This app uses LangChain and Streamlit to create a ChatGPT-like experience.")

# Sidebar for API Key input
openai_api_key = st.sidebar.text_input("🔑 Enter your OpenAI API Key", type="password")

# Function to generate response
def generate_response(query):
    try:
        llm_model = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm_model.invoke(query)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

# Layout using columns for better UI
col1, col2 = st.columns([3, 1])

with col1:
    with st.form("query_form"):
        text = st.text_area("💬 Enter your query:", placeholder="Type your question here...")
        submitted = st.form_submit_button("Submit")

    if not openai_api_key.startswith("sk-"):
        st.warning("⚠ Please enter a valid OpenAI API key.", icon="⚠")

    if submitted and openai_api_key.startswith("sk-"):
        if text.strip():
            with st.spinner("🤖 Generating response..."):
                response = generate_response(text)
                st.success("Response received!")
                st.write(response)
        else:
            st.error("Please enter some text before submitting.")

# Sidebar or column for additional info or instructions
with col2:
    st.info("Instructions: Enter your OpenAI API key on the left sidebar. Then, input a query in the text box and click 'Submit'.")

