import streamlit as st
import pandas as pd
from io import StringIO

st.title('Task 5: 파일 업로드')

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

    st.subheader('데이터 구조')
    st.write(df.head())

    st.subheader('데이터 요약')
    st.write(df.describe())



st.title('Task 6: 레이아웃 구성')

col1, col2 = st.columns(2)
col1.write("컬럼 1")
col2.write("컬럼 2")