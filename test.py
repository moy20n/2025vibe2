import streamlit as st
import random
import time

st.set_page_config(page_title="🎮 숫자/논리 게임 센터", layout="centered")
st.title("🎮 숫자/논리 게임 센터")
st.markdown("💡 원하는 게임을 선택해서 즐겨보세요!")

# 고급 게임 선택
game_list = {
    "🔢 업다운 게임": "업다운 게임",
    "🧠 기억력 테스트": "기억력 테스트",
    "🧮 2048 미니버전": "2048 미니버전",
    "🖼 틀린 그림 찾기": "틀린 그림 찾기"
}
game_display = st.selectbox("🎲 게임을 선택하세요", list(game_list.keys()))
game_choice = game_list[game_display]

# ------------------------
# 🔢 업다운 게임
# ------------------------
if game_choice == "업다운 게임":
    st.subheader("🔢 업다운 게임")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.last_result = ""
        st.session_state.game_over = False
        st.session_state.ranking = []

    if not st.session_state.game_over:
        guess = st.number_input("1부터 100 사이 숫자를 입력하세요", 1, 100, step=1)
        if st.button("확인"):
            st.session_state.tries += 1
            if guess < st.session_state.secret_number:
                st.session_state.last_result = "🔺 더 높은 숫자입니다!"
            elif guess > st.session_state.secret_number:
                st.session_state.last_result = "🔻 더 낮은 숫자입니다!"
            else:
                st.session_state.last_result = f"🎉 정답입니다! {st.session_state.tries}번 만에 맞췄어요."
                st.session_state.game_over = True
                st.balloons()

    st.info(st.session_state.last_result)

    if st.session_state.game_over:
        name = st.text_input("🎉 이름을 입력하고 랭킹에 도전하세요!", key="rank_name")
        if st.button("랭킹에 등록하기"):
            if name:
                st.session_state.ranking.append((name, st.session_state.tries))
                st.session_state.ranking.sort(key=lambda x: x[1])
                st.success("✅ 랭킹 등록 완료!")
                # 초기화
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.tries = 0
                st.session_state.last_result = ""
                st.session_state.game_over = False
            else:
                st.warning("이름을 입력해주세요!")

    if st.session_state.ranking:
        st.subheader("🏆 TOP 5 랭킹")
        for i, (n, t) in enumerate(st.session_state.ranking[:5], start=1):
            st.markdown(f"**{i}위. {n}** — ⏱ {t}번 시도")

# ------------------------
# 🧠 기억력 테스트
# ------------------------
elif game_choice == "기억력 테스트":
    st.subheader("🧠 기억력 테스트")

    # 초기 상태 설정
    if "memory_game_stage" not in st.session_state:
        st.session_state.memory_game_stage = "start"  # "show", "input", "done"
        st.session_state.memory_sequence = ""
        st.session_state.memory_start_time = 0.0
        st.session_state.memory_ranking = []
        st.session_state.memory_result = ""

    # 게임 시작
    if st.session_state.memory_game_stage == "start":
        st.write("👁 숫자를 보고 기억하세요!")
        if st.button("게임 시작"):
            num_digits = random.randint(4, 6)
            st.session_state.memory_sequence = "".join([str(random.randint(0, 9)) for _ in range(num_digits)])
            st.session_state.memory_game_stage = "show"
            st.session_state.memory_start_time = time.time()
            st.experimental_rerun()

    # 숫자 잠깐 보여줌
    elif st.session_state.memory_game_stage == "show":
        st.markdown(f"### 👉 기억하세요: `{st.session_state.memory_sequence}`")
        time.sleep(2.5)  # 2.5초 후 가림
        st.session_state.memory_game_stage = "input"
        st.experimental_rerun()

    # 입력 단계
    elif st.session_state.memory_game_stage == "input":
        st.write("😶 숫자가 사라졌어요! 기억나는 숫자를 입력하세요.")
        answer = st.text_input("기억한 숫자 입력", max_chars=6)
        if st.button("제출"):
            end_time = time.time()
            duration = round(end_time - st.session_state.memory_start_time, 2)
            if answer == st.session_state.memory_sequence:
                st.success(f"정답! ⏱ {duration}초 만에 맞췄어요.")
                st.session_state.memory_result = f"{duration}초 성공"
                st.session_state.memory_game_stage = "done"
                st.session_state.memory_last_time = duration
            else:
                st.error(f"틀렸어요! 정답은 `{st.session_state.memory_sequence}` 였습니다.")
                st.session_state.memory_result = "실패"
                st.session_state.memory_game_stage = "start"

    # 랭킹 등록
    elif st.session_state.memory_game_stage == "done":
        name = st.text_input("이름을 입력하고 랭킹에 등록하세요!", key="memory_rank_name")
        if st.button("랭킹 등록"):
            if name:
                st.session_state.memory_ranking.append((name, st.session_state.memory_last_time, len(st.session_state.memory_sequence)))
                st.session_state.memory_ranking.sort(key=lambda x: x[1])  # 시간 기준
                st.success("✅ 랭킹에 등록되었습니다!")
                st.session_state.memory_game_stage = "start"
            else:
                st.warning("이름을 입력해주세요!")

    # 랭킹 표시
    if st.session_state.memory_ranking:
        st.subheader("🏆 기억력 테스트 TOP 5")
        for i, (n, t, d) in enumerate(st.session_state.memory_ranking[:5], start=1):
            st.markdown(f"**{i}위. {n}** — {d}자리 / ⏱ {t}초")

# ------------------------
# 나머지 개발 예정 게임
# ------------------------
elif game_choice == "2048 미니버전":
    st.subheader("🧮 2048 미니버전 (개발 중)")
    st.info("👉 이 게임은 곧 추가될 예정입니다!")

elif game_choice == "틀린 그림 찾기":
    st.subheader("🖼 틀린 그림 찾기 (개발 중)")
    st.info("👉 이 게임은 곧 추가될 예정입니다!")
