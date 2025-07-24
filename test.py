import pyautogui
import random
import time

# 클릭할 좌표 범위 설정 (왼쪽 위, 오른쪽 아래)
x_min, x_max = 100, 500
y_min, y_max = 200, 600

# 클릭 횟수와 간격
click_count = 20
delay = 0.5  # 초 단위

print(f"시작 3초 후 무작위 클릭 {click_count}회 실행합니다...")
time.sleep(3)

for i in range(click_count):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
    print(f"{i+1}번째 클릭: ({x}, {y})")
    time.sleep(delay)

print("✅ 클릭 완료!")

