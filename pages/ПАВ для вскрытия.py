import streamlit as st
import pandas as pd

st.title("ПАВ для первичного вскрытия продуктивных пластов")
st.sidebar.success("ПАВ")
#col1, col2 = st.columns(2)
ing_1 = st.checkbox('Концентрат неионных ПАВ для первичного вскрытия')
ing_2 = st.checkbox('Композия ПАВ и полиспиртов для вскрытия и освоения коллекторов')

df = pd.read_excel('База реагенты.xlsx')

if ing_1:
    st.error(df['Название'][16])
    st.warning(df['Описание'][16])
    st.success(df['Цена'][16])
if ing_2:
    st.error(df['Название'][17])
    st.warning(df['Описание'][17])
    st.success(df['Цена'][17])
