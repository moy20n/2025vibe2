import streamlit as st
import random
import time

def memory_game():
    st.subheader("🧠 기억력 테스트")

    # 초기화
    if "memory_stage" not in st.session_state:
        st.session_state.memory_stage = "ready"
        st.session_state.memory_sequence = ""
        st.session_state.memory_start_time = 0.0
        st.session_state.memory_last_time = 0.0
        st.session_state.memory_ranking = []

    # 단계 1: 숫자 생성 및 표시
    if st.session_state.memory_stage == "ready":
        if st.button("🟢 숫자 보기"):
            num_digits = random.randint(4, 6)
            st.session_state.memory_sequence = "".join([str(random.randint(0, 9)) for _ in range(num_digits)])
            st.session_state.memory_stage = "show"
            st.session_state.memory_start_time = time.time()

    if st.session_state.memory_stage == "show":
        st.markdown(f"### 👁 기억하세요: `{st.session_state.memory_sequence}`")
        if st.button("✅ 다 외웠어요!"):
            st.session_state.memory_stage = "input"

    if st.session_state.memory_stage == "input":
        answer = st.text_input("📝 기억한 숫자를 입력해 보세요:")
        if st.button("제출"):
            end_time = time.time()
            duration = round(end_time - st.session_state.memory_start_time, 2)
            if answer == st.session_state.memory_sequence:
                st.success(f"🎉 정답입니다! ⏱ {duration}초 걸렸어요.")
                st.session_state.memory_last_time = duration
                st.session_state.memory_stage = "result"
            else:
                st.error(f"❌ 틀렸어요! 정답은 `{st.session_state.memory_sequence}` 입니다.")
                st.session_state.memory_stage = "ready"

    if st.session_state.memory_stage == "result":
        name = st.text_input("이름을 입력하세요", key="memory_name")
        if st.button("🏆 랭킹 등록"):
            if name:
                st.session_state.memory_ranking.append((name, st.session_state.memory_last_time, len(st.session_state.memory_sequence)))
                st.session_state.memory_ranking.sort(key=lambda x: x[1])  # 빠른 순
                st.success("✅ 등록 완료!")
                st.session_state.memory_stage = "ready"
            else:
                st.warning("이름을 입력해주세요.")

    if st.session_state.memory_ranking:
        st.subheader("🏅 기억력 랭킹 (TOP 5)")
        for i, (n, t, d) in enumerate(st.session_state.memory_ranking[:5], 1):
            st.markdown(f"{i}위. **{n}** — {d}자리 / ⏱ {t}초")

