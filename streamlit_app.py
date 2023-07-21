import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.write('Firsts *Steps!* :sunglasses:')


st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 3

#df = pd.DataFrame({
#    'first column': [1, 2, 3],
#     'second column': [age, 2 * age, 3 * age]
#     })
#st.write(df)

# Example 5
random_array = np.random.randn(age, 4)
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

st.header('Line chart')

chart_data = pd.DataFrame(
     rounded_array,
     columns=['a', 'b', 'c', 'd'])

st.line_chart(chart_data)

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2023, 7, 22, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)