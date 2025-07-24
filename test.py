import streamlit as st
import random

st.set_page_config(page_title="🎮 숫자/논리 게임 센터", layout="centered")
st.title("🎮 숫자/논리 게임 센터")
st.markdown("👉 왼쪽 사이드바에서 게임을 선택하세요!")

# 게임 선택
game_choice = st.sidebar.radio("게임을 선택하세요:", ["업다운 게임", "2048 미니버전", "틀린 그림 찾기", "기억력 테스트"])

# 업다운 게임
if game_choice == "업다운 게임":
    st.subheader("🔢 업다운 게임")
    
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.last_result = ""

    guess = st.number_input("1부터 100 사이 숫자를 입력하세요", 1, 100, step=1)
    
    if st.button("확인"):
        st.session_state.tries += 1
        if guess < st.session_state.secret_number:
            st.session_state.last_result = "🔺 더 높은 숫자입니다!"
        elif guess > st.session_state.secret_number:
            st.session_state.last_result = "🔻 더 낮은 숫자입니다!"
        else:
            st.balloons()
            st.success(f"🎉 정답입니다! {st.session_state.tries}번 만에 맞췄어요.")
            if st.button("게임 다시 시작하기"):
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.tries = 0
                st.session_state.last_result = ""
    
    if st.session_state.last_result:
        st.info(st.session_state.last_result)

# 2048 미니버전 자리표시자
elif game_choice == "2048 미니버전":
    st.subheader("🧮 2048 미니버전 (개발 중)")
    st.info("👉 이 게임은 곧 추가될 예정입니다!")

# 틀린 그림 찾기 자리표시자
elif game_choice == "틀린 그림 찾기":
    st.subheader("🖼 틀린 그림 찾기 (개발 중)")
    st.info("👉 이 게임은 곧 추가될 예정입니다!")

# 기억력 테스트 자리표시자
elif game_choice == "기억력 테스트":
    st.subheader("🧠 기억력 테스트 (개발 중)")
    st.info("👉 이 게임은 곧 추가될 예정입니다!")
