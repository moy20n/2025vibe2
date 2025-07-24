import streamlit as st
import random

st.set_page_config(page_title="✊✋✌ 가위바위보 게임", page_icon="🎮")

st.title("✊✋✌ 가위바위보 게임")
st.write("당신의 선택은? 아래 버튼을 눌러보세요!")

choices = ["가위", "바위", "보"]
user_choice = st.radio("선택하기:", choices, horizontal=True)

if st.button("대결 시작!"):
    computer_choice = random.choice(choices)

    st.write(f"🤖 컴퓨터의 선택: **{computer_choice}**")

    # 승패 판정
    if user_choice == computer_choice:
        result = "😐 무승부!"
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        result = "🎉 당신이 이겼습니다!"
    else:
        result = "💥 컴퓨터가 이겼습니다!"

    st.success(result)

