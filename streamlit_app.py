import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

st.title('Google Gemini Chat App')

PASSWORD = st.sidebar.text_input('Enter password', type='password')

def generate_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    st.info(model.generate_content("What is the meaning of life?").text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the meaning of life?')
    submitted = st.form_submit_button('Submit')
    if not PASSWORD == "password":
        st.warning('Please enter the password!', icon='⚠')
    if submitted and PASSWORD == "password":
        generate_response(text)
