import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

import os

# Load OpenAI API Key from Streamlit Secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the OpenAI client
client = OpenAI(api_key=openai_api_key)

# Streamlit app UI
st.set_page_config(page_title="Ghulam's AI Chatbot", page_icon="🤖")
st.title("🤖 Ghulam's AI Chatbot")
st.markdown("Ask anything, and I’ll try my best to help!")

# Text input box
user_input = st.text_input("💬 Your question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content
            st.success("🤖 Reply:")
            st.write(reply)
        except Exception as e:
            st.error("Oops! Something went wrong. Please try again.")
            st.exception(e)
