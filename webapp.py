import streamlit as st
import requests

st.title("БОТ ПОМОШНиК")
st.write("НС которая посчитает потраченные калории за тренировку")

with st.form("Подача данных"):
    gender = st.radio("Пол", ['Male', 'Female'])
    if gender == 'Male':
        Male = 1
        Female = 0
    else:
        Male = 0
        Female = 1
    Age = st.number_input('Ваш возраст', min_value=12)
    Height = st.number_input('Ваш рост', min_value=1)
    Weight = st.number_input('Ваш вес', min_value=1)
    Duration = st.number_input('Время тренировки (в минутах)', min_value=1)
    sabmit = st.form_submit_button('Провести вычисления')
    
if sabmit:
    data = {'Male': Male, 'Female': Female, 'Age': Age, 'Height': Height, 'Weight': Weight, 'Duration': Duration}
    response = requests.post('https://ml-for-calculate-calories.onrender.com', json=data)
    st.success(f'Потраченные калории: {response.json():.0f}')