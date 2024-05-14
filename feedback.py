import streamlit as st
import pandas as pd

def app():
    
    st.header(':mailbox: Send us your feedback!')
    st.write('Do you have suggestion or found some bug?')
    st.write('let us know in the field bellow.')

    contact_form = """
    <form action="https://formsubmit.co/princykakadiya152@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Describe your experience here..." required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html= True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

app()