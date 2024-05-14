import streamlit as st
import auth

def registration_ui():
    email = st.text_input('Email Address')
    password = st.text_input('Password',type = 'password')
    username = st.text_input('Enter your unique username')

    if st.button('Create my account'):
        user= auth.create_user(email = email, password = password, uid = username)

        st.success('Account created successfully!')
        st.markdown('Please login using your email and password')
        st.balloons()