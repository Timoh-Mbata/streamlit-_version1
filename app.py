import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import json
import joblib as jb
import os
from matplotlib.font_manager import json_load
# import the model
model_path = r"C:\Users\user\Desktop\streamlit\streamlit-_version1\churn_model.joblib"
model = jb.load(model_path)
column_path = r"C:\Users\user\Desktop\streamlit\streamlit-_version1\Regions"
# columns = np.load(column_path)
st.title('WELCOME TO CHURN PREDICTION APP')
st.text('This are the available Regions : ')
st.text(json_load(column_path))
region = st.number_input('ENTER THE REGION USING THERE NUMBERS')
# allowing the user inputs :
# MONTANT
montant = st.number_input('ENTER THE MONTANT : ')
# FREQUENCE_RECH
frech = st.number_input('ENTER THE FREQUENCE_RECH : ')
# REVENUE
revenue = st.number_input('ENTER THE REVENUE : ')
arpu = st.number_input('ENTER THE ARPU_SEGMENT : ')
frec =st.number_input('ENTER THE FREQUENCE : ')
data_vol = st.number_input('ENTER THE DATA_VOLUME : ')
if st.button("predict"):
    features = [[region,montant,frech,revenue,arpu,frec,data_vol]]
    expected = model.predict(features)
    if expected == 1:
        st.write('left')
    else :
        st.write('remained')
