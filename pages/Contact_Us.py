import streamlit as st
import pandas
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact Us")

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email message: ")

    user_topic = st.selectbox(
        "What topic would you like to discuss?",
        df["topic"]
    )

    raw_message = st.text_area("Your message")

    # Backslash and LB required when including subject in email text
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {user_topic}
{raw_message}
    """

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent")