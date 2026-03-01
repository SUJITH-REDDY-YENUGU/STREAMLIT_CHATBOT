import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Sidebar model selector
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Choose Groq model",
    ["llama-3.1-8b-instant", "llama-3.1-70b-instant", "gemma2-9b-it"]
)

# Initialize ChatGroq with selected model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name=model_choice
)

# Define prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "{question}")
])

# Chain: prompt → LLM → parser
chain = prompt | llm | StrOutputParser()

# --- Streamlit Frontend ---
st.set_page_config(page_title="ChatGroq Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 ChatGroq AI Chatbot")
st.markdown("Ask me anything — powered by **LangChain + Groq**.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response
    try:
        response = chain.invoke({"question": user_input})
    except Exception as e:
        response = f"⚠️ Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
