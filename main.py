import streamlit as st

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



