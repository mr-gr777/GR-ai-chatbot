import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Assuming you are using Gemini API
from gemini import Gemini  # Replace this with the actual Gemini package if it exists

# Load Gemini API Key from Streamlit Secrets
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Initialize the Gemini client (Adjust if Gemini uses a different client structure)
client = Gemini(api_key=gemini_api_key)

# Streamlit app UI setup
st.set_page_config(page_title="Ghulam's AI Chatbot", page_icon="🤖")
st.title("🤖 Ghulam's AI Chatbot")
st.markdown("Ask anything, and I’ll try my best to help!")

# Text input box
user_input = st.text_input("💬 Your question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            # Adjust the method to match Gemini's API call structure
            response = client.chat.completions.create(
                model="gemini-1.5-turbo",  # Adjust according to Gemini's model name
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content  # Adjust based on actual Gemini API response structure
            st.success("🤖 Reply:")
            st.write(reply)
        except Exception as e:
            st.error("Oops! Something went wrong. Please try again.")
            st.exception(e)
