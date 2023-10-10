import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!!")

col1,col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

st.checkbox("Checkbox I Agree")
st.multiselect("Multiselect",["Option 1","Option 2","Option 3"])

DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
nrows=1000
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data.rename(columns={'Lat': 'LAT', 'Lon': 'LON'})
    #st.dataframe(data)
    return data

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
#* optional kwarg unsafe_allow_html = True

st.map(load_data(nrows).loc[:, ['LAT', 'LON']])
