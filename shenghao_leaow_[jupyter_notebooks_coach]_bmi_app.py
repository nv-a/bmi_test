# -*- coding: utf-8 -*-
"""Shenghao Leaow - [Jupyter Notebooks - Coach] BMI_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10b5ExHB9DlmPTLfUFnyIAbQ1imirb_wC

<font size="+3">Module 48 - BMI App</font>

## Context: Understanding the Problem Statement --------Problem Scoping

#### BMI Calculator

Body Mass Index (BMI) is generally used to broadly categorize a person as underweight, normal weight, overweight, or obese based on their height and weight.
For calculating the BMI, we need to know the Weight (in Kg) and Height (in metre) .

#### Import the Streamlit Library
"""

import streamlit as st

"""#### Give title to the application and ask user for entering height and weight for calculating BMI"""

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Enter your height in Centimeters')

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Enter your height in Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input('Enter your height in Feet')

    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

"""#### Classify the BMI index of the person based on the WHO chart

![who_chart.jpg](attachment:who_chart.jpg)
"""

# check if the button is pressed or not
if(st.button('Calculate BMI')):

    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))

    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")

