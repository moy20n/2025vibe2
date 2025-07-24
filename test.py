import streamlit as st
import time
import random

st.title("⚡ 순발력 테스트 ⚡")

if "started" not in st.session_state:
    st.session_state.started = False
if "show_button" not in st.session_state:
    st.session_state.show_button = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0.0

def start_game():
    st.session_state.started = True
    st.session_state.show_button = False
    delay = random.uniform(2, 5)
    time.sleep(delay)
    st.session_state.start_time = time.time()
    st.session_state.show_button = True
    st.experimental_rerun()

def button_clicked():
    reaction_time = time.time() - st.session_state.start_time
    st.success(f"🎉 반응속도: {int(reaction_time * 1000)} ms")
    st.session_state.started = False
    st.session_state.show_button = False

if not st.session_state.started:
    st.button("🟢 시작하기", on_click=start_game)
elif st.session_state.show_button:
    st.button("⚡ 지금 클릭!", on_click=button_clicked)
else:
    st.info("⏳ 준비 중... 버튼이 뜨면 바로 눌러!")
