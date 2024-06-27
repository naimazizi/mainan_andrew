from openai import OpenAI
import streamlit as st

def get_result(prompt):
    # This is a placeholder URL. Replace it with your actual API endpoint.
    return "Your text is probably an AI - Generated Text with probability of 69%"

st.title("💬 AI Generated Text Detector")
st.caption("🚀 AI Generated Text Detector for Data Science Thesis")
st.caption("Made By: 2501961994 - Andrew Widjaya")

user_input = st.text_area("Your text here")

if st.button("Get Response"):
    if user_input:
        with st.spinner("Getting response from ..."):
            result = get_result(user_input)
            st.write("**Response from the model:**")
            st.write(result)
    else:
        st.write("Please enter some text to get a response.")