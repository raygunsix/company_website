import streamlit as st

st.set_page_config(layout="wide")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email message: ")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print("Pressed")