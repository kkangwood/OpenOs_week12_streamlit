import streamlit as st
import pandas as pd
from io import StringIO

#--------------Task 1------------------

# 타이틀
st.title('Streamlit 기본 실습')
st.markdown('### Task1: 기본 UI컴포넌트')

# text 입력
st.text_input("이름을 입력하세요")
# 슬라이더
st.slider('나이',min_value=0,max_value=100,value=23)

# 선택 박스
st.selectbox('좋아하는 색',['빨강🔴','파랑🔵','노랑😊','초록📗'])

st.checkbox('이용 약관에 동의합니다')
if st.button('제출'):
    st.success("제출이 완료되었습니다!!😊😎")


#-----------------Task 2-------------------

df1 = pd.read_csv('penguins.csv')

st.markdown('### Task1: 기본 UI컴포넌트')
st.dataframe(df1.head())

#-----------------Task 4------------------------

from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.write("Task4")
df = pd.read_csv('penguins.csv')

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df

st.dataframe(filter_dataframe(df))

#--------------------Task 5------------------------------
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

st.set_page_config(
    page_title = 'Team5 os week12 Streamlit Practice',
    page_icon='😶‍🌫️'
)
