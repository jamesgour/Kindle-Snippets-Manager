# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns

import sys
import io
import streamlit as st

# File uploader
uploaded_file = st.file_uploader("Upload File Here")

# Read uploaded file to a dataframe
clippings_df = pd.read_csv(uploaded_file, header=None, sep='\n')

# Turn df into list of lists based on snippet groups for easier transformation into clean data frame
clippings_list_final = []
temp_list = []

for index, row in clippings_df[0].items():
    if row == '==========':
        clippings_list_final.append(temp_list)
        temp_list = []
    else:
        temp_list.append(row)

# Create a new data frame from the list of lists
clippings_df = pd.DataFrame(clippings_list_final)

# Merge clippings that flow onto multiple lines into one column
clippings_df['Clipping'] = clippings_df[clippings_df.columns[2:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

# Remove the extra columns & rename
clippings_df = clippings_df[[0, 1, 'Clipping']]
clippings_df.columns = ['Book Title', 'Metadata', 'Clipping']

# Expand the Book Title & Metadata info into individual columns
clippings_df[['Book Title','Author']] = clippings_df['Book Title'].str.split('(', expand=True)
clippings_df['Author'] = clippings_df['Author'].str.replace(')', '')

# Derive a Location column & Page column (if applicable)
clippings_df['Location'] = clippings_df['Metadata'].str.extract(r'(Location \d+)')
clippings_df['Page'] = clippings_df['Metadata'].str.extract(r'(page \d+)')
clippings_df['Date Added'] = clippings_df['Metadata'].str.extract(r'(Added on .+)')
clippings_df['Date Added'] = clippings_df['Date Added'].str.replace('Added on ', '')
# Still need to turn Date Added column into a date time

# Remove duplicate clippings - sometimes happens due to Kindle glitch
print(len(clippings_df))
clippings_df = clippings_df.drop_duplicates(subset='Clipping', keep="last")
print(len(clippings_df))
clippings_df = clippings_df.drop_duplicates(subset=['Location', 'Author'], keep="last")
print(len(clippings_df))

st.write(clippings_df)


