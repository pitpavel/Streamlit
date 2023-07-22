import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

def userdatasection():

    st.header('Your information')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('How old are you?', 0, 130, 25)

    with col2:
        color = st.selectbox(
            'What is your favorite color?',
            ['Green', 'Yellow', 'Red', 'Blue', 'Black'])

    with col3:
        animals = st.multiselect(
            'What are your favorite animals',
            ['Dog', 'Cat', 'Pinguin', 'Rabbit'])
    user_params = {
        'age': age,
        'color': color,
        'animals': animals
    }
    return user_params


def ordersection():
    st.markdown(coloredtext_markdown('Order', userdata['color']), unsafe_allow_html=True)

    st.write('What would you like to order?')
    col1, col2, col3 = st.columns(3)

    with col1:
        icecream = st.checkbox('Ice cream')
    with col2:
        coffee = st.checkbox('Coffee')
    with col3:
        cola = st.checkbox('Cola')

    if icecream:
        st.write("Great! Here's some more 🍦")

    if coffee:
        st.write("Okay, here's some coffee ☕")

    if cola:
        st.write("Here you go 🥤")


def coloredtext_markdown(text, color):
    return f'<h2 style="color:{color}">{text}</h2>'

# Установка стиля для всех заголовков на странице
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

st.header('Firsts *Steps!* :sunglasses:')

# Example 1

userdata = userdatasection()

# Order section

ordersection()

# Example 3
st.markdown(coloredtext_markdown('Randoms', userdata['color']), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

random_array = np.random.randn(userdata['age'], 4)
scaled_array = (random_array + 0) * 100
rounded_array = scaled_array.astype(int)
df2 = pd.DataFrame(
    rounded_array,
    columns=['a', 'b', 'c', 'd'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c', 'd'])
with col1:
    st.write(c)

chart_data = pd.DataFrame(
    rounded_array,
    columns=['a', 'b', 'c', 'd'])

with col2:
    st.line_chart(chart_data)

df = pd.DataFrame(rounded_array, columns=['a', 'b', 'c', 'd'])
with col3:
    st.write(df)

# Example 2

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

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
