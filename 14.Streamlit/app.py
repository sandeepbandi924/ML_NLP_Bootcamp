import streamlit as st
import pandas as pd
import numpy as np

##Title ofthe application
st.title('Hello Streamlit')

##Display Simple Text
st.write('This is a simple text')

##Create a simple DataFrame
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

##Display the DataFrame
st.write('Here is the DataFrame')
st.write(df)

##create a line chart
chart_data =pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart()