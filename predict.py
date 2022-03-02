import streamlit as st
import pandas as pd
import pickle
def app():
    option_basket = st.sidebar.selectbox(
     'Did the customer add any item to the basket?',
    ('Yes', 'No'))
    option_promo = st.sidebar.selectbox(
     'Did the customer click on any Promo banner?',
    ('Yes', 'No'))
    option_sign_in = st.sidebar.selectbox(
     'Did the customer sign in?',
    ('Yes', 'No'))
    option_home = st.sidebar.selectbox(
     'Did the customer see the home page?',
    ('Yes', 'No'))
    option_repeat = st.sidebar.selectbox(
     'Is he a repeating customer?',
     ('Yes', 'No'))
    if st.sidebar.button('Predict the Possibility of the Customer to make a purchase'):
        lookup_dict={"Yes":1,"No":0}
        dict = {'basket_add_detail':[lookup_dict[option_basket]],
            'promo_banner_click':[lookup_dict[option_promo]],
            'sign_in':[lookup_dict[option_sign_in]],
            "saw_homepage":[lookup_dict[option_home]],
            "returning_user":[lookup_dict[option_repeat]]
           }
        prediction_df = pd.DataFrame(dict)
        st.write("Customer details for Propensity prediction")
        st.write(prediction_df)
        with open("propensity_model.pkl", 'rb') as pfile:  
            propensity_model_loaded=pickle.load(pfile)
        y_predicted=propensity_model_loaded.predict(prediction_df)
        if (y_predicted[0]==1):
            st.write("The customer will order from the website. Probabality of ordering:")
            # st.write(y_predicted[0])
        else:
            st.write("The customer will not order from the website. Probabality of ordering:")
            # st.write(y_predicted[0])
        st.write(propensity_model_loaded.predict_proba(prediction_df))
