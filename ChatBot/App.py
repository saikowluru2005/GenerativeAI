import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

# System role
message = [
    SystemMessage(content="You are a funny AI agent")
]

# Streamlit UI
st.title("🤖 Funny AI Chatbot")

# Chat input
text = st.chat_input("Type your message...")

if text:
    # User role
    message.append(HumanMessage(content=text))

    # AI response
    response = model.invoke(message)

    # AI role
    message.append(AIMessage(content=response.text))

    # Display user message
    with st.chat_message("user"):
        st.write(text)

    # Display AI message
    with st.chat_message("assistant"):
        st.write(response.text)