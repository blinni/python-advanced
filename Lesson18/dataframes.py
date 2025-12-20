import pandas as pd
import streamlit as st

st.header("Display dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 26, 34, 44, 31],
    'City': ['New York', 'Los Angelos', 'Chicago', 'Houston', 'Phoneix']
})

st.dataframe(data)