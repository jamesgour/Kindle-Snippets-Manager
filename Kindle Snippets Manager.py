# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns

import sys
import io
import streamlit as st

# File uploader
uploaded_file = st.file_uploader("Upload File Here")

# Create Pandas DataFrame from myclippings.txt file
#def SnippetDataFrame(uploaded_file):
    # Create a list item for every line in myclippings.txt

# Create a list item for every line in myclippings.txt
clippings_list = []

if uploaded_file is not None:
    for line in uploaded_file:
        #line = line.replace('\n', '')
        #line = line.replace('\ufeff', '')
        #clippings_list.append(line)
        st.write(line)

# LEFT OFF HERE - still trying to figure out how to read line by line when the uploaded file is read in bytes!!

# with open('My Clippings - Copy.txt', 'r+', encoding="utf8") as file:
#     for line in file:
#         line = line.rstrip('\n')
#         line = line.replace('\ufeff', '')
#         clippings_list.append(line)



# Remove empty lines from list
for item in clippings_list:
    if item == '':
        clippings_list.remove(item)
    else:
        pass


# Re-package into list of lists for each item ending at separator "=========="
clippings_list_final = []
temp_list = []

for item in clippings_list:
    if item == '==========':
        clippings_list_final.append(temp_list)
        temp_list = []
    else:
        temp_list.append(item)

# clippings_list_final

# Create a data frame from the list
clippings_df = pd.DataFrame(clippings_list_final)

# Merge clippings that flow onto multiple lines into one column
clippings_df['Clipping'] = clippings_df[clippings_df.columns[2:]].apply(lambda x: ' '.join(x.dropna().astype(str)),
                                                                        axis=1)

# Remove the extra columns & rename
clippings_df = clippings_df[[0, 1, 'Clipping']]
clippings_df.columns = ['Book Title', 'Metadata', 'Clipping']

# Remove duplicate clippings - sometimes happens due to Kindle glitch
clippings_df = clippings_df.drop_duplicates(subset='Clipping', keep="first")

# Expand the Book Title & Metadata info into individual columns
clippings_df[['Book Title', 'Author']] = clippings_df['Book Title'].str.split('(', expand=True)
clippings_df['Author'] = clippings_df['Author'].str.replace(')', '')


