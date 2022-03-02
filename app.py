# Simple Multi-Page Web Application using Streamlit

import streamlit as st
import training
import predict

#Title of the Application
st.title("Predict Customer's Purchase")


#Choice of page
page_choices={"Know more about the training data":training,
              "Predict the Possibility of Purchase":predict}


#Create radio button for the page choice
page_selection = st.radio("Go to", list(page_choices.keys()))


#Choosing the page based on the user selection from radio button
page = page_choices[page_selection]


#Display the page
with st.spinner(f'Loading {page_selection} ...'):
    page.app()

