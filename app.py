import google.generativeai as genai
import streamlit as st
import os

# Get API from local new
key=os.getenv('GOOGLE_API_KEY')

#configure the model
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

#create a frontend UI
st.title('SIMPLE TEXT GENERATION')
st.header('This to test the gemini model as application')
prompt=st.text_input("write your prompt here:",max_chars=1000)
if prompt:
    response=model.generate_content(prompt)
    st.write(response.text)