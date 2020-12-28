# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns

# Import Streamlit
import streamlit as st

# Streamlit Slider
x = st.slider('x')
st.write(x, 'squared is', x*x)

# Text Input
url = st.text_input('Enter URL')
st.write('The Entered URL is now', url)
