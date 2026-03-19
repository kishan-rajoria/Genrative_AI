from langchain import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.header("Langchain Prompts UI")

st.text_input("Enter your prompt here", key="prompt")

if st.button("Submit"):
    st.text("Processing...")