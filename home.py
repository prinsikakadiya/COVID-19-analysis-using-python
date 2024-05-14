import streamlit as st

# Get query parameters
query_params = st.experimental_get_query_params()

# Check if the 'page' parameter is set to 'home'
if 'page' in query_params and query_params['page'] == ['home']:
    st.header("Welcome to the home page")







# import streamlit as st
# import streamlit_authenticator as stauth
# import datetime
# import re

# def validate_email(email):
#     pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1-3}$"

#     if re.match(pattern,email):
#         return True
#     return False

# def validate_username(username):
#     pattern = "^[a-zA-Z0-9]*$"
#     if re.match(pattern,username):
#         return True
#     return False

# def sign_uo():
#     with st.form(key='signup', clear_on_submit=True):
#         st.subheader(':green[Sign Up]')
#         email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
#         username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
#         password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
#         password2 = st.text_input(':blue[Confirm] Password', placeholder='Confirm Your Password', type='password')


    
#         btn1, bt2, btn3, btn4, btn5 = st.columns(5)

#         with btn3:
#             sign_up = st.form_submit_button('Sign Up')

#         return sign_up

# sign_up = sign_uo() 

# if sign_up:
#     st.subheader('HELLO')


# import streamlit as st
# import re

# def validate_email(email):
#     pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
#     return re.match(pattern, email)

# def validate_username(username):
#     pattern = "^[a-zA-Z0-9]*$"
#     return re.match(pattern, username)

# def sign_up():
#     with st.form(key='signup', clear_on_submit=True):
#         st.subheader(':green[Sign Up]')
#         email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
#         username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
#         password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
#         password2 = st.text_input(':blue[Confirm] Password', placeholder='Confirm Your Password', type='password')

#         submitted = st.form_submit_button('Sign Up')

#         if submitted:
#             if validate_email(email) and validate_username(username) and password1 == password2:
#                 st.write("Welcome to home page")
#             else:
#                 st.write("Please fill in the form correctly")

# sign_up()   

