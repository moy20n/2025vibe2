import streamlit as st
import random
import os

st.set_page_config(page_title="가위바위보", page_icon="✊")

# 캐릭터 정보
characters = {
    "코난": {"image": "aff4843c-42d0-405b-a4f5-84b652ebaf3b.png", "quote": "내 이름은 에도가와 코난. 이번 판도 이길 수밖에 없겠군."},
    "유미란": {"image": "3a7906e1-bd19-4814-8b9e-7cfedee8fe0c.png", "quote": "좋아, 나 진지하게 한다? 질 생각은 없어."},
    "하인성": {"image": "01d3ed05-3cde-4b19-ae9b-ee96f7fde093.png", "quote": "이런 승부, 정면 돌파가 답이지. 바로 간다!"},
    "유명한": {"image": "992f5417-8ff8-4fda-bcdb-f8bc919af83f.png", "quote": "이 게임, 촉이 중요해. 오늘은 느낌이 아주 좋아."},
    "진": {"image": "1b30170d-2dbe-42f7-8fe5-8da6380280fa.png", "quote": "방해하지 마. 이긴다. 끝."},
    "베르무트": {"image": "1fa94a84-362c-4486-b626-1918cc5f7f20.png", "quote": "흥미롭군. 과연 어느 쪽이 웃게 될까?"},
    "남도일": {"image": "3c6c5ca1-483c-42de-81dc-ff620a3827e5.png", "quote": "한 번에 끝내주지. 명탐정은 지지 않아."},
    "괴도키드": {"image": "d777fb30-5934-4baf-ae74-69f62316d192.png", "quote": "승부는 한 순간의 판단. 넌 그걸 넘을 수 있을까?"},
    "홍장미": {"image": "70150bc9-d99c-494a-961f-c529f187fb2f.png", "quote": "이번엔 무조건 이길 거야. 각오해."},
    "안기준": {"image": "cf778a0e-b611-488a-9d11-5ac101406dd4.png", "quote": "분석 완료. 승리는 정해졌다."},
    "이상윤": {"image": "9138035e-33e4-42f6-b3f1-fa2749456a40.png", "quote": "목표 설정 완료. 이제 실행할 차례다."},
    "정보라": {"image": "796ce44a-247c-4470-ac76-259e28864526.png", "quote": "나도 진심으로 한다. 결과는 곧 알게 되겠지."},
    "서가영": {"image": "d3b4b95b-0c84-4af5-83dd-af8729a9b544.png", "quote": "좋아, 어디 한번 붙어보자. 심심하던 참이야."},
    "골롬보 반장님": {"image": "6cdd0662-6b68-43eb-b289-1688fa0a8d18.png", "quote": "어떤 사건도 이 촉을 피하지 못하지. 시작하지."},
    "브라운 박사님": {"image": "4da19e0c-cdf7-46cd-a95e-40ec7118d4ce.png", "quote": "이런 게임도 실험처럼 신중해야지. 준비됐나?"}
}

choices = ["가위", "바위", "보"]

# 세션 초기화
if "score" not in st.session_state:
    st.session_state.score = {"승": 0, "패": 0, "무": 0}
if "ranking" not in st.session_state:
    st.session_state.ranking = {name: {"승": 0, "패": 0, "무": 0} for name in characters}
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "last_enemy" not in st.session_state:
    st.session_state.last_enemy = None

st.title("✊ 가위바위보 대전!")
st.subheader("🎮 상대를 선택하세요!")

opponent = st.selectbox("상대 선택", list(characters.keys()))
op_data = characters[opponent]

# 이미지 로딩
img_path = f"image/{op_data['image']}"
if os.path.exists(img_path):
    st.image(img_path, width=300, caption=opponent)
else:
    st.warning("⚠️ 이미지가 없어요. images 폴더에 파일을 넣어주세요.")

st.info(op_data['quote'])

# 선택
user_choice = st.radio("당신의 선택은?", choices, horizontal=True)

if st.button("대결 시작!"):
    enemy_choice = random.choice(choices)

    # 결과 판정
    if user_choice == enemy_choice:
        result = "무"
        msg = "😐 무승부!"
    elif (
        (user_choice == "가위" and enemy_choice == "보") or
        (user_choice == "바위" and enemy_choice == "가위") or
        (user_choice == "보" and enemy_choice == "바위")
    ):
        result = "승"
        msg = "🎉 당신이 이겼습니다!"
    else:
        result = "패"
        msg = "💥 당신이 졌습니다!"

    # 기록
    st.session_state.last_result = (user_choice, enemy_choice, msg)
    st.session_state.last_enemy = opponent
    st.session_state.score[result] += 1
    st.session_state.ranking[opponent][result] += 1

# 결과 표시
if st.session_state.last_result:
    uc, ec, msg = st.session_state.last_result
    st.markdown(f"🧑 당신: **{uc}**")
    st.markdown(f"🎭 {st.session_state.last_enemy}: **{ec}**")
    st.success(msg)

# 점수판
st.divider()
st.subheader("📊 당신의 총 전적")
s = st.session_state.score
st.write(f"✔ 승: {s['승']}  ❌ 패: {s['패']}  🤝 무: {s['무']}")

# 랭킹
st.subheader("📈 상대별 랭킹")
for name, record in st.session_state.ranking.items():
    st.write(f"**{name}** - 승: {record['승']}, 패: {record['패']}, 무: {record['무']}")
