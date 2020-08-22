from flask import Flask,render_template,url_for,request
import pandas as pd 

import pickle
import streamlit as st

# classifier=pickle.load(pickle_in)
# load the model from disk
loaded_model=pickle.load(open('Random_forest_regressor.pkl', 'rb'))
# app = Flask(__name__)

# # @app.route('/')
# def home():
# 	return render_template('home.html')

# @app.route('/predict',methods=['POST'])
def predict(Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Average_visibility):
    prediction = loaded_model.predict([[Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Average_visibility]])
    return prediction


def main():
    st.title("DELHI AIR QUALITY PREDICTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">DELHI AIR QUALITY PREDICTION APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Average_Temp = st.text_input("Average_Temp","Type Here")
    Max_Temp= st.text_input("Max_Temp","Type Here")
    Min_Temp = st.text_input("Min_Temp","Type Here")
    Atm_Pressure = st.text_input("Atm_Pressure","Type Here")
    Average_visibility = st.text_input("Average_visibility","Type Here") 
    result=""
    if st.button("Predict the Air Quality"):
        result=predict(Average_Temp,Max_Temp,Min_Temp,Atm_Pressure,Average_visibility)
    st.success('Predicted PM2.5 for today is {}'.format(result))
    if st.button("About"):
        st.text("Developed By KARNDEEP SINGH")
        st.text("Manipal Academy Of Higher Education")

if __name__=='__main__':
    main()
