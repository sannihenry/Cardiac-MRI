# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""
import streamlit as st
from PIL import Image
image = Image.open('b2ap3_amp_human-anatomy-with-heart.jpg')
st.image(image, caption='Cardiac: With a healthy heart the beat goes on')

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("Cclassifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(LVEDV,LVESV,LVM_diastole,LVM_indexed,LVEDV_indexed,LVESV_indexed,LVSV,LVSV_indexed,RVM,RVM_indexed,Gender):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: LVEDV
        in: query
        type: number
        required: true
      - name: LVESV
        in: query
        type: number
        required: true
      - name: LVM_diastole
        in: query
        type: number
        required: true
      - name: LVM_indexed
        in: query
        type: number
        required: true
      - name: LVEDV_indexed
        in: query
        type: number
        required: true
      - name: LVESV_indexed
        in: query
        type: number
        required: true
      - name: LVSV
        in: query
        type: number
        required: true
      - name: LVSV_indexed
        in: query
        type: number
        required: true
      - name: RVM
        in: query
        type: number
        required: true
      - name: RVM_indexed
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[LVEDV,LVESV,LVM_diastole,LVM_indexed,LVEDV_indexed,LVESV_indexed,LVSV,LVSV_indexed,RVM,RVM_indexed,Gender]])
    print(prediction)
    return prediction



def main():
    st.title("COVID 19 Prediction Software (CARDIAC MRI)")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Check your COVID 19 status today </h2>
    </div>

    <div style="background-color:tomato;padding:10px">
    <h3 style="color:yellow;text-align:left;">Result: </h3>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h4 style="color:yellow;text-align:left;">1-You have COVID 19 </h4>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h5 style="color:yellow;text-align:left;">0-You are free from the VIRUS </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    LVEDV = st.text_input("LVEDV","Type Here")
    LVESV = st.text_input("LVESV","Type Here")
    LVM_diastole = st.text_input("LVM_diastole","Type Here")
    LVM_indexed = st.text_input("LVM_indexed","Type Here")
    LVEDV_indexed = st.text_input("LVEDV_indexed","Type Here")
    LVESV_indexed = st.text_input("LVESV_indexed","Type Here")
    LVSV = st.text_input("LVSV","Type Here")
    LVSV_indexed = st.text_input("LVSV_indexed","Type Here")
    RVM = st.text_input("RVM","Type Here")
    RVM_indexed = st.text_input("RVM_indexed","Type Here")
    Gender = st.text_input("Gender","input (1) for male and (0) for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(LVEDV,LVESV,LVM_diastole,LVM_indexed,LVEDV_indexed,LVESV_indexed,LVSV,LVSV_indexed,RVM,RVM_indexed,Gender)
    st.success('Your COVID 19 Chances {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by Henry")

if __name__=='__main__':
    main()
    
    
    