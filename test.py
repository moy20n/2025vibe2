# clicker.py
import pyautogui
import random
import time
import sys

# 명령줄 인수로 좌표/횟수/딜레이 받기
x_min = int(sys.argv[1])
x_max = int(sys.argv[2])
y_min = int(sys.argv[3])
y_max = int(sys.argv[4])
click_count = int(sys.argv[5])
delay = float(sys.argv[6])

print("3초 후 시작합니다...")
time.sleep(3)

for i in range(click_count):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
    print(f"{i+1}번째 클릭: ({x}, {y})")
    time.sleep(delay)

print("✅ 완료!")
