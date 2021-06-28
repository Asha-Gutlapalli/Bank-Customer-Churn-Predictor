import streamlit as st

# this caches the output to store the output and not call this function again
# and again preventing time wastage. `allow_output_mutation = True` tells the
# function to not hash the output of this function and we can get away with it
# because no arguments are passed through this.
# https://docs.streamlit.io/en/stable/api.html#streamlit.cache
@st.cache(allow_output_mutation=True, show_spinner=False)
def get_models():
  from predictor import Predictor
  return {
    'Predictor' : Predictor()
  }

# load all the models before the app starts
with st.spinner('Loading Model...'):
  MODELS = get_models()

# description
st.markdown("# :bank: Bank Customer Churn Predictor :money_with_wings:")
st.write('''
Customer churn, also known as customer attrition, occurs when customers \
stop doing business with a company. The companies are interested in \
identifying segments of these customers because the price for acquiring \
a new customer is usually higher than retaining the old one. A Deep Neural \
Network is employed to achieve this task. A Deep Neural Network is an \
Artificial Neural Network that has multiple hidden layers in between the input and output layers.
''')

# instruction
st.markdown("## :pencil2: **Please fill the form** :pencil2:")
model = MODELS['Predictor']

with st.form("Customer Details"):
    # credit score
    score = st.number_input('Credit Score', value=792)
    # country
    country = st.text_input('Country', 'Spain')
    # gender
    gender = st.selectbox(label="Gender", options=["Male", "Female"], index=1)
    # age
    age = st.number_input('Age', value=28)
    # tenure
    tenure = st.number_input('Tenure', value=4)
    # balance
    balance = st.number_input('Balance', value=130142.79)
    # num of products
    number_products = st.number_input('Number of Products', value=1)
    # credit card status
    card = st.selectbox(label="Do they have a credit card?", options=["Yes", "No"], index=0)
    # active member status
    active = st.selectbox(label="Are they an active member?", options=["Yes", "No"], index=1)
    # estimated salary
    salary = st.number_input('Expected Salary', value=38190.78)
    # classes
    classes = {"Yes" : 1, "No" : 0}
    # data
    data = [[score, country, gender, age, tenure, balance, number_products, classes[card], classes[active], salary]]
    # predict
    button = st.form_submit_button("Predict")


# predict churn probability
if button:
  with st.spinner('Predicting...'):
    msg, image_name = model.predict(data)
    # display message
    st.markdown(msg)
    # display emoji
    st.image(f"assets/{image_name}.png")
