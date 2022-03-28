# A-streamlit-application-to-predict-customer's-purchase-using-ML-model

# Aim:
The aim of this project is to build a Machine Learning model that predicts the customer's possibility of purchase using historical data. Each website has a lot of visitors every day but not all of them make a purchase. Instead of spending money to target such visitors using digital marketing like social media platforms, it makes sense to optimize this activity by targeting real valuable prospects who are more likely to make a purchase.

# About dataset:
For simplicity we use a shortest version of the dataset. The columns that we choose for this task are given below:

'UserID' – Unique Identifier for each customer

'basket_add_detail' – A binary variable indicating if the customer added an item to the basket from the product detail page

'promo_banner_click' – A binary variable indicating if the customer clicked on any promotional banners

'sign_in' – Another binary variable, indicating if the customer signed into our website

'returning_user' – Again, a binary variable indicating if the customer is a returning visitor to our website

'saw_homepage' – A binary variable indicating if the customer saw the homepage of the website

'ordered' – Our target variable. A binary variable indicating if the customer placed an order

**The dataset is highly imbalanced so the prediction will be biased. To solve this problem, we have used undersampling technique. Undersampling is a technique to balance uneven datasets by keeping all of the data in the minority class and decreasing the size of the majority class.**

# Streamlit Webapp:
The final output is a Streamlit Application that takes in particular customer inputs and predicts the probability that a customer with those inputs will make a purchase or not.

`To run the app use below command:`

**`streamlit run app.py`**
