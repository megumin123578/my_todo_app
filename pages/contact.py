import streamlit as st
from send_email import send

st.header('Contact me')

with st.form(key = 'email_form'):
    user_email = st.text_input(' Your email address')
    message = st.text_area('Your message')
    button = st.form_submit_button('Submit')
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{message}"""
    if button:

        send(message)
        st.info("Your email was sent successfully !")
