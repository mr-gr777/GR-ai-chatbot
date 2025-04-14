import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Ghulam's AI Chatbot")

# User input
user_input = st.text_input("Ask me anything:")

# Chat history (simple)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# On input, get response
if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You're a helpful assistant."},
                *st.session_state.chat_history,
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.success(reply)