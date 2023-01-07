# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:37:19 2022

@author: Afroz
"""

import streamlit as st

primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"


def header(url):
 st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
 
# giving a title
color = st.color_picker('Pick A Color', '#00f900')
title = '<p style="font-family:Lucida Calligraphy; color:Brown; font-size: 45px;">Heart Disease Prediction</p>'
st.markdown(title, unsafe_allow_html=True)

# Method 1
st.markdown(f'<h1 style="color:Brown;font-size:24px;">{"Color Me Blue text"}</h1>', unsafe_allow_html=True)
 
# Method 2
title = '<p style="font-family:Lucida Calligraphy; color:Brown; font-size: 45px;">Heart Disease Prediction</p>'
st.markdown(title, unsafe_allow_html=True)

message = st.text_area("Message", height=100)
st.title(message)

password = st.text_input("Enter Password", type='password')
st.title(password)

my_date = st.date_input("Select date") 
st.write(my_date)

base="light"

my_time = st.time_input("Select time")

Age = st.text_input('Age of the Person')

# Image import
from PIL import Image
img = Image.open("C:/Users/Afroz/Desktop/Streamlit Test/Best Code Streamlit/Heart Disease/Heart.jpg")
st.image(img, width=700)