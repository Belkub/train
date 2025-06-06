import streamlit as st
import pandas as pd

st.title("Ингибирующие добавки для буровых растворов")
st.sidebar.success("Ингибиторы набухания глин")
col1, col2 = st.columns(2)
ing_1 = col1.checkbox('Полигликоли')
ing_2 = col1.checkbox('Ингибитор набухания активных глин')
ing_3 = col1.checkbox('Суперингибитор активных глин и аргиллитов')
ing_4 = col2.checkbox('Аминный ингибитор')
ing_5 = col2.checkbox('ГКЖ')
ing_6 = col2.checkbox('Ингибитор для акриловых растворов')

df = pd.read_excel('База реагенты.xlsx')

if ing_1:
    st.error(df['Название'][0])
    st.warning(df['Описание'][0])
    st.success(df['Цена'][0])
if ing_2:
    st.error(df['Название'][1])
    st.warning(df['Описание'][1])
    st.success(df['Цена'][1])
if ing_3:
    st.error(df['Название'][2])
    st.warning(df['Описание'][2])
    st.success(df['Цена'][2])
if ing_4:
    st.error(df['Название'][3])
    st.warning(df['Описание'][3])
    st.success(df['Цена'][3])
if ing_5:
    st.error(df['Название'][4])
    st.warning(df['Описание'][4])
    st.success(df['Цена'][4])
if ing_6:
    st.error(df['Название'][5])
    st.warning(df['Описание'][5])
    st.success(df['Цена'][5])
