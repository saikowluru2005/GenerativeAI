import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash')

# Bot mood
mood = st.text_input("Enter mood of bot:")

if mood:
    setMood = f'You are a {mood} AI agent'

    # Initialize messages
    if "message" not in st.session_state:
        st.session_state.message = [
            SystemMessage(content=setMood)
        ]

    st.title("🤖 AI Chatbot")

    # Display previous messages
    for msg in st.session_state.message:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # User input
    text = st.chat_input("You:")

    if text:
        # Human role
        st.session_state.message.append(
            HumanMessage(content=text)
        )

        # Get AI response
        response = model.invoke(st.session_state.message)

        # AI role
        st.session_state.message.append(
            AIMessage(content=response.text)
        )

        # Display response
        with st.chat_message("user"):
            st.write(text)

        with st.chat_message("assistant"):
            st.write(response.text)