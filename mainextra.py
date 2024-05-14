import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re

def validate_email(email):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1-3}$"

    if re.match(pattern, email):
        return True
    return False

def validate_username(username):
    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False

def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
        password2 = st.text_input(':blue[Confirm] Password', placeholder='Confirm Your Password', type='password')

        btn1, btn2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            if st.form_submit_button('Sign Up'):
                # Redirect to the home page
                st.experimental_set_query_params(page="home")
                
sign_up()
