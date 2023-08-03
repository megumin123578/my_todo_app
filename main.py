import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image("miku.jpg")
with col2: 
    st.title('HEHE')
    content = """
Learn PyTorch. Become a Deep Learning Engineer. Get Hired.
"""
    st.info(content)

content2 = """
The third film based on Marvel's Guardians of the Galaxy."""
st.write(content2)

col3, col4 = st.columns(2)
df = pd.read_csv('006 data.csv', sep = ';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])