# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns

import sys
import io
import streamlit as st

# SIDEBAR UI
# Title for the app
st.sidebar.title('Kindle Snippets Manager')
st.sidebar.write('A simpler way to remember what you read')

# Email Address Input
email_address = st.sidebar.text_input("Please enter e-mail address for daily summary")

# Number of random quotes to receive
num_quotes = st.sidebar.selectbox('How many quotes would you like to receive?', range(11))

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload the myclippings.txt file here")


# MAIN APP PAGE
# Title for the app
st.title("Today's Daily Snippets")


# Function for cleaning & transforming txt file into dataframe
@st.cache
def create_dataframe(file):
    # Read uploaded file to a dataframe
    clippings_df = pd.read_csv(file, header=None, sep='\n')

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
    clippings_df['Clipping'] = clippings_df[clippings_df.columns[2:]].apply(lambda x: ' '.join(x.dropna().astype(str)),
                                                                            axis=1)

    # Remove the extra columns & rename
    clippings_df = clippings_df[[0, 1, 'Clipping']]
    clippings_df.columns = ['Book Title', 'Metadata', 'Clipping']

    # Expand the Book Title & Metadata info into individual columns
    clippings_df[['Book Title', 'Author']] = clippings_df['Book Title'].str.split('(', expand=True)
    clippings_df['Author'] = clippings_df['Author'].str.replace(')', '')

    # Derive a Location column & Page column (if applicable)
    clippings_df['Location'] = clippings_df['Metadata'].str.extract(r'(Location \d+)')
    clippings_df['Page'] = clippings_df['Metadata'].str.extract(r'(page \d+)')
    clippings_df['Date Added'] = clippings_df['Metadata'].str.extract(r'(Added on .+)')
    clippings_df['Date Added'] = clippings_df['Date Added'].str.replace('Added on ', '')
    # Still need to turn Date Added column into a date time

    # Remove duplicate clippings & clean up odd entries - sometimes happens due to Kindle glitch
    clippings_df = clippings_df.drop_duplicates(subset='Clipping', keep="last")
    clippings_df = clippings_df.drop_duplicates(subset=['Location', 'Author'], keep="last")
    clippings_df = clippings_df.dropna(subset=['Date Added'])

    return clippings_df




# Run create_dataframe function
clippings_df = create_dataframe(uploaded_file)

# # Display DataFrame
# if uploaded_file is not None:
#     st.write(clippings_df)

# START OF RANDOM SELECTION CODE
# Method 1: Pick num_quotes at random
clippings_df_len = len(clippings_df)
random_selection = np.random.randint(clippings_df_len, size=num_quotes)
random_selection_df = clippings_df.iloc[random_selection]
random_selection_df = random_selection_df[['Book Title', 'Author', 'Clipping']]
# Add in validation to avoid getting the same quote multiple times!!

# Print the quotes
for index, row in random_selection_df.iterrows():
    st.write('_________________________________')
    st.write(row['Book Title'] + '- ' + row['Author'])
    st.write(row['Clipping'])





#st.write(])

# # Method 2: Select a random book and then num_quotes # of random quotes
#
# # Create dict of book titles & number of quotes per title
# book_titles = clippings_df['Book Title'].unique()
# num_quotes = {}
#
# for title in book_titles:
#     num_quotes[title] = (len(clippings_df[clippings_df['Book Title'] == title]))
#
# # Generate num_quotes random quotes based on 1) random selection of a book and 2)random selection of num_quotes quotes
# # If the book does not have num_quotes quotes, pick another book and generate the remaining amount of quotes
# num_of_titles = len(book_titles)



