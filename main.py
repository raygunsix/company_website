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

with col1:
    st.write("Name")
    st.write("Title")
    st.write("Photo")

with col2:
    st.write("Name")
    st.write("Title")
    st.write("Photo")

with col3:
    st.write("Name")
    st.write("Title")
    st.write("Photo")