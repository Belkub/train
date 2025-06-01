import streamlit as st
import pandas as pd

st.title("Смазочные композиции для буровых растворов")
st.sidebar.success("Смазочные добавки")
#col1, col2 = st.columns(2)
ing_1 = st.checkbox('Универсальная премиальная смазка')
ing_2 = st.checkbox('Смазка класса medium для полимерных (соленасыщенных, хлоркалиевых) и полимер-глинистых растворов')
ing_3 = st.checkbox('Смазка класса lite для глинистых и полимер-глинистых растворов')
ing_4 = st.checkbox('Смазочная добавка для РУО класса standart')
ing_5 = st.checkbox('Смазочная добавка для РУО класса lite')

df = pd.read_excel('D:\\Users\\файлы\\train\\pages\\База реагенты.xlsx')

if ing_1:
    st.error(df['Название'][6])
    st.warning(df['Описание'][6])
    st.success(df['Цена'][6])
if ing_2:
    st.error(df['Название'][7])
    st.warning(df['Описание'][7])
    st.success(df['Цена'][7])
if ing_3:
    st.error(df['Название'][8])
    st.warning(df['Описание'][8])
    st.success(df['Цена'][8])
if ing_4:
    st.error(df['Название'][9])
    st.warning(df['Описание'][9])
    st.success(df['Цена'][9])
if ing_5:
    st.error(df['Название'][10])
    st.warning(df['Описание'][10])
    st.success(df['Цена'][10])
