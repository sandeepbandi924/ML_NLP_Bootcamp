import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')

name = st.text_input('Enter your name:')

age = st.slider('Select your age:',0,100,25)

options = ['Python','Java','C++','JavaScript']
choice = st.selectbox('Choose your favorite language:',options)
st.write(f'You selected {choice}')

st.write(f'Your age is {age}')
if name:
    st.write(f'Hell, {name}')


data = {
    'Name':['Sandeep','Sumanth','Varun','Tharun'],
    'Age':[26,22,24,28],
    'City':['Hyderabad','New York','Bangalore','Thailand']
}
df = pd.DataFrame(data)
df.to_csv('sample.csv')
st.write(df)

upload_file= st.file_uploader('Choose a csv file',type='csv')

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)