import streamlit as st
from streamlit_extras.colored_header import colored_header

colored_header(
    label="Main Page",
    description=" ",
    color_name="violet-70",
)

st.info("Welcome to the website for the project, here you can look at the information and view the map by clicking on a page on the left hand side.")

st.sidebar.success("Please select a page.")