import streamlit as st
import google.generativeai as genai

st.title('Google Gemini Chat App')

GOOGLE_API_KEY = st.sidebar.text_input('Google API Key', type='password')

def generate_response(input_text):
    model = genai.GenerativeModel("gemini-pro")
    st.info(model.generate_content("What is the meaning of life?").text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the meaning of life?')
    submitted = st.form_submit_button('Submit')
    if not GOOGLE_API_KEY.startswith('AIza'):
        st.warning('Please enter your Google API key!', icon='⚠')
    if submitted and GOOGLE_API_KEY.startswith('AIza'):
        generate_response(text)
