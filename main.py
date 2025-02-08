import streamlit as st
import pandas as pd



st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/SaiKarthikKagolanu.jpg", width = 300)

with col2:
    st.title("Sai Karthik Kagolanu")
    content= """
    Hi, I am Karthik! I am MSc Robotics graduate from The University of Sheffield with an undergraduate degree in BTech 
    Mechanical Engineering from Vellore Institute of Technology. I am highly passionate about robotics, automation and
    mechanisms and often invest time to learn more on integrating these into technology. 
    """

    st.info(content)

contact = """Below you can find some of the apps I have built using Python. Feel free to contact me!"""
st.info(contact)

col3, col4 = st.columns(2)

data = pd.read_csv("data.csv", sep=";")
with col3:
    for index,row in data[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])

with col4:
    for index,row in data[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])

