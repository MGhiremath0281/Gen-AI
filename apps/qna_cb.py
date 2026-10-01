import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("Gemini AI Chatbot")

query = st.text_input("Enter your question")

if st.button("Ask"):
    if query:
        res = llm.invoke(query)
        st.write("### AI:")
        st.write(res.content)