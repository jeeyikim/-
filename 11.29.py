# app.py
import streamlit as st
import pandas as pd

st.title("대학생의 경제 상황과 소비 패턴에 따른 만족도 분석을 위한 설문지")

# 섹션 1: 기본 정보
st.header("1. 기본 정보")
name = st.text_input("이름을 입력하세요:")
gender = st.radio("성별을 선택하세요:", ("남성", "여성", "기타"))
age = st.number_input("만 나이를 입력하세요:", min_value=0, max_value=120, step=1)
major = st.text_input("학과를 입력하세요(공식명칭으로 써주세요. 예: 아시아언어문명학부):")
residence = st.radio("주거 형태를 선택하세요:", ("자취", "기숙사", "통학", "기타"))

# 섹션 2: 수입원
st.header("2. 수입원")
work_hour = st.number_input("일주일 기준 총 알바 시간이 얼마인가요? (단위: 시간)")
salary = st.number_input("한달에 알바를 통해 받는 돈은 얼마인가요? (단위: 만 원)")
work_satisfaction = st.slider("알바에 대한 만족도는 얼마인가요? (1: 매우 불만족, 5: 매우 만족):", 1, 5)
pocketmoney = st.number_input("월 평균 용돈은 얼마인가요? (단위: 만 원)")

# 섹션 3: 지출
st.header("3. 지출")
food = st.number_input("월 평균 식비 지출은 얼마인가요? (단위: 만 원)")
transportation = st.number_input("월 평균 교통 지출은 얼마인가요? (단위: 만 원)")
house = st.number_input("월세는 얼마인가요? (단위: 만 원)")
living_etc = st.number_input("기타 생활비 지출은 얼마인가요? (단위: 만 원)")
saving = st.number_input("월 저축은 얼마인가요? (단위: 만 원)")
leisure = st.number_input("월 평균 여가비 지출은 얼마인가요? (단위: 만 원)")
sudden = st.number_input("월 평균 충동 구매 횟수는 얼마인가요? (단위: 회)")

# 섹션 4: 만족도
st.header("4. 만족도")
satisfaction = st.slider("경제적 만족도 (1: 매우 불만족, 5: 매우 만족):", 1, 5)
reason = st.text_area("만족도에 대한 이유를 간결하게 적어주세요.")

# 데이터 저장 및 출력
if st.button("제출"):
    response_data = {
        "이름": name,
        "나이": age,
        "성별": gender,
        "전공": major,
        "주거형태": residence,
        "알바시간": work_hour,
        "월급": salary,
        "알바만족도": work_satisfaction,
        "용돈": pocketmoney,
        "식비": food,
        "교통비": transportation,
        "월세": house,
        "기타생활비": living_etc,
        "여가비": leisure,
        "월저축": saving,
        "충동구매횟수": sudden,
        "만족도": satisfaction,
        "이유": reason
    }
    response_df = pd.DataFrame([response_data])
    response_df.to_csv("survey_responses.csv", mode="a", header=False, index=False)
    st.success("설문지가 제출되었습니다. 감사합니다!")
    st.write("제출된 데이터:")
    st.write(response_df)
