# #[theme]
# base="dark"
# primaryColor="#ea3b3b"
# backgroundColor="#15151c"
# secondaryBackgroundColor="#606069"

import streamlit as st

from streamlit_option_menu import option_menu 
import vaccine, overview, patient, patient2, feedback, auth

def main():
        
        with st.sidebar:
            choice= option_menu(
                 menu_title = None,
                 options = ["Account","Patient(india)","Patient(statewise)","Vaccine","Overview","Feedback"]
            )
      #icacls example.txt /grant:r $env:USERNAME:F

        if choice =='Account':
            auth.app()

        if choice =='Patient(india)':
            patient.app()
            
        elif choice =='Vaccine':
            vaccine.app()

        elif choice =='Overview':
            overview.app()  

        elif choice =='Patient(statewise)':
            patient2.app() 

        elif choice == 'Feedback':
            feedback.app() 
    

if __name__ == '__main__':
      main()          

 




