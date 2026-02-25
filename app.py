import streamlit as st
from backend.prompts import SYSTEM_PROMPT
from backend.memory import initialize_memory, update_memory
from backend.gemini_service import generate_response

st.set_page_config(page_title="🏥 Healthcare Information Bot")

st.title("🏥 Healthcare Information Chatbot")
st.markdown(
    "⚠️ This chatbot provides general health information only. "
    "It is not a substitute for professional medical advice."
)

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Display chat history
for message in st.session_state.chat_history[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("How are you feeling today..?"):

    # Emergency check
    emergency_keywords = ["chest pain", "suicidal", "difficulty breathing"]

    if any(word in prompt.lower() for word in emergency_keywords):
        st.error("⚠️ Please seek immediate medical attention.")
    else:
        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.chat_history.append(
            {"role": "user", "content": prompt}
        )

        with st.spinner("Analyzing symptoms..."):
            response = generate_response(st.session_state.chat_history)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": response}
        )