import pandas as pd 

import pickle
import streamlit as st

loaded_model=pickle.load(open('Random_forest_regressor.pkl', 'rb'))

def predict(Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Average_humidity,Average_visibility,
            Average_windspeed,Maximum_sustained_windspeed):
    prediction = loaded_model.predict([[Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Average_humidity,Average_visibility,
                                        Average_windspeed, Maximum_sustained_windspeed]])
    return prediction


def main():
    st.title("DELHI AIR QUALITY PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">DELHI AIR QUALITY PREDICTION APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Average_Temp = st.text_input("Average_Temp(°C)","Type Here")
    Max_Temp= st.text_input("Max_Temp (°C)","Type Here")
    Min_Temp = st.text_input("Min_Temp (°C)","Type Here")
    Atm_Pressure = st.text_input("Atm_Pressure (mm)","Type Here")
    Atm_humidity = st.text_input("Atm_humidity(%)", "Type Here")
    Average_visibility = st.text_input("Average_visibility(Km)","Type Here")
    Average_windspeed = st.text_input("Average_windspeed(Km/h)", "Type Here")
    Maximum_sustained_windspeed = st.text_input("Maximum_sustained_windspeed(Km/h)", "Type Here")
    result=""
    if st.button("Predict the Air Quality"):
        result=predict(Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Atm_humidity,Average_visibility,
                       Average_windspeed,Maximum_sustained_windspeed)
    st.success('Predicted PM2.5 for today is {}'.format(result))
    if st.button("About"):
        st.text("Developed By Yachna Hasija")

if __name__=='__main__':
    main()

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[2],[3]])
c=a+b
print(c)

a=np.random.randn(3,3)
b=np.random.rand(3,1)
c=a*b
print(c)
