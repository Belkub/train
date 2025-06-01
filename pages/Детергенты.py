import streamlit as st
import pandas as pd

st.title("Противосальниковые добавки")
st.sidebar.success("Детергенты")
#col1, col2 = st.columns(2)
ing_1 = st.checkbox('Противосальниковая композиция неионных ПАВ')
ing_2 = st.checkbox('Противосальиковый и ингибирующий комплекс на основе окисленных аминов')

df = pd.read_excel('/main/pages/База реагенты.xlsx')

if ing_1:
    st.error(df['Название'][14])
    st.warning(df['Описание'][14])
    st.success(df['Цена'][14])
if ing_2:
    st.error(df['Название'][15])
    st.warning(df['Описание'][15])
    st.success(df['Цена'][15])
