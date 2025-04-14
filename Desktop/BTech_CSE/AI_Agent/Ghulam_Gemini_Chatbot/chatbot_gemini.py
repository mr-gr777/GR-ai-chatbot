import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 Gemini Chatbot")
user_input = st.text_input("You:", "")

if user_input:
    response = model.generate_content(user_input)
    st.markdown(f"**Bot:** {response.text}")
