import streamlit as st
import pandas as pd
import numpy as np

st.write("My very first app\nLet's see what we can do")

x_series = np.arange(0,100)
y_series = np.random.uniform(0, 10, 100)

data = pd.DataFrame({'column_x': x_series, 'column_y': y_series})

st.line_chart(data)
