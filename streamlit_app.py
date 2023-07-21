import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 6],
     'second column': [10, 20, 30, 40, 66]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
random_array = np.random.randn(100, 4)
min_value = 0
max_value = 100
scaled_array = (random_array + 0) * 100
rounded_array = scaled_array.astype(int)
df2 = pd.DataFrame(
     rounded_array,
     columns=['a', 'b', 'c', 'd'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c', 'd'])
st.write(c)

