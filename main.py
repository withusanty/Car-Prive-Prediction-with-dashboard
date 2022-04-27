import streamlit as st
import numpy as np
import pickle
from PIL import Image

im = Image.open("car.png")
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon=im,
    layout="wide",
)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("Follow @ ")
with col2:
    st.markdown("[Linkedin](https://www.linkedin.com/in/santy707)")
with col3:
    st.markdown("[Kaggle](https://www.kaggle.com/kuchhbhi)")
with col4:
    st.markdown("[Github](https://github.com/withusanty)")
with col5:
    st.markdown("[Tableau](https://public.tableau.com/app/profile/santosh.kumar3246)")

col1, col2, col3, col4= st.columns(4)
with col1:
    st.markdown("Checkout Other Projects:  ")
with col2:
    st.markdown("[Stock Price Analysis](https://stock-analysis-santosh.herokuapp.com/)")
with col3:
    st.markdown("[WhatsApp Chat Analysis](https://whatsapp-santosh.herokuapp.com/)")
with col4:
    st.markdown("[Movie Recommender](https://santy-movierecommend.herokuapp.com/)")


col1,col2,col3 = st.columns([1.5,3,1])
with col2:
     st.title('Car Price Prediction')

year = np.arange(2004,2023).tolist()
year.reverse()

model = pickle.load(open('rf_model.pkl', 'rb'))

Present_Price = 0
Kms_Driven = 0
Owner = 0
How_Old	= 0
Fuel_Type_Diesel = 0
Fuel_Type_Petrol = 0
Seller_Type_Individual = 0
Transmission_Manual = 0

col1,col2 = st.columns(2)
with col1:
     price = st.text_input('Present Price of the Car?', placeholder='Enter the  price...',max_chars=7)

with col2:
     drivenkms = st.text_input('How much car has been driven in KMs?', placeholder='Enter the  KMs driven...',max_chars=6)

years = st.select_slider(
          'Car Built Year?',
          options=year)

col1, col2 = st.columns(2)
with col1:
     fuel = st.selectbox(
          "Fuel Type?",
          ('Select Fuel Type...', 'Petrol', 'Diesel', 'CNG'))

with col2:
     seller = st.selectbox(
          "Seller Type?",
          ('Select Seller Type...', 'Dealer', 'Individual'))


col1,col2 = st.columns(2)
with col1:
     transmission = st.selectbox(
          "Transmission Type?",
          ('Select Transmission Type...','Automatic', 'Manual'))

with col2:
     owner = st.selectbox(
          "Owner Type?",
          ('Select Owner Type...',0,1,2,3))

data = np.array([Present_Price, Kms_Driven, Owner, How_Old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]).reshape(1,8)

col1,col2,col3 = st.columns([3,3,1])
with col2:
     if st.button('Predict Price!!'):
          try:
               if price != 'Enter the  price...':
                    Present_Price = int(price) / 100000
               Kms_Driven = drivenkms
               How_Old = 2022 - years

               if fuel == 'Petrol':
                    Fuel_Type_Diesel = 0
                    Fuel_Type_Petrol = 1
               elif fuel == 'Diesel':
                    Fuel_Type_Diesel = 1
                    Fuel_Type_Petrol = 0
               elif fuel == 'CNG':
                    Fuel_Type_Diesel = 0
                    Fuel_Type_Petrol = 0

               if seller == 'Dealer':
                    Seller_Type_Individual = 0
               elif seller == 'Individual':
                    Seller_Type_Individual = 1

               if transmission == 'Automatic':
                    Transmission_Manual = 0
               if transmission == 'Manual':
                    Transmission_Manual = 1
               Owner = owner

               data = np.array(
                    [Present_Price, Kms_Driven, Owner, How_Old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
                     Transmission_Manual]).reshape(1, 8)
               # st.write(np.array([data]).reshape(1,8))

               p = model.predict(np.array([data]).reshape(1,8))[0] * 100000
               st.metric(f'Predicted Price Rs.', int(p))
          except:
               st.text('Oops... \nKindly check the inputs.')