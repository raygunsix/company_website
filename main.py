import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(description)

st.header("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        first_name = row['first name']
        last_name =  row['last name']
        st.header(f"{first_name.title()} {last_name.title()}")
        st.write(row['role'])
        st.write("Photo")

with col2:
    for index, row in df[4:8].iterrows():
        first_name = row['first name']
        last_name =  row['last name']
        st.header(f"{first_name.title()} {last_name.title()}")
        st.write(row['role'])
        st.write("Photo")

with col3:
    for index, row in df[8:].iterrows():
        first_name = row['first name']
        last_name =  row['last name']
        st.header(f"{first_name.title()} {last_name.title()}")
        st.write(row['role'])
        st.write("Photo")