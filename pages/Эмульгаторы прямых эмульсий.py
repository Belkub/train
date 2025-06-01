import streamlit as st
import pandas as pd

st.title("Эмульгаторы прямых и биконтинуальных микроэмульсий")
st.sidebar.success("Эмульгаторы")
#col1, col2 = st.columns(2)
ing_1 = st.checkbox('Эмульгатор класса standart')
ing_2 = st.checkbox('Соэмульгатор для повышения термостойкости и солестойкости прямых эмульсий')
ing_3 = st.checkbox('Эмульгатор класса premium')


df = pd.read_excel('База реагенты.xlsx')

if ing_1:
    st.error(df['Название'][11])
    st.warning(df['Описание'][11])
    st.success(df['Цена'][11])
if ing_2:
    st.error(df['Название'][12])
    st.warning(df['Описание'][12])
    st.success(df['Цена'][12])
if ing_3:
    st.error(df['Название'][13])
    st.warning(df['Описание'][13])
    st.success(df['Цена'][13])
