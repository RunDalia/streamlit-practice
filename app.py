import streamlit as st
datalist = [100, 50, 30]
st.write('# First Data List')
st.write('## Raw Data')
datalist
st.write('## Bar Chart')
st.bar_chart(datalist)
import pandas as pd
sview = pd.Series(datalist)
sview
