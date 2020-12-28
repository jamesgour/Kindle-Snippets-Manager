#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns

# Import Streamlit
import streamlit as st


# In[5]:


x = st.slider('x')
st.write(x, 'squared is', x*x)


# In[ ]:




