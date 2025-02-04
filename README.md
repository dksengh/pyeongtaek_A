# 코드
import math
import cv2
import os
import tkinter as tk
from tkinter import simpledialog
from ultralytics import YOLO, solutions

# YOLO 모델 로드
model = YOLO("yolov8x.pt")

# GUI 창을 통해 사용자 입력 받기
root = tk.Tk()
root.withdraw()  # 기본 창 숨기기
status = " "
person_count = " "

width = simpledialog.askfloat("입력", "넓이를 입력하세요:")
angle = simpledialog.askfloat("입력", "기울기를 입력하세요:")

# 입력값 출력
print(f"입력된 값 - 넓이: {width}, 기울기: {angle}")

# 이미지 파일 경로 설정
image_path = './project/Dublin, Ireland.png'

# 모델 예측 수행
results = model(image_path)

# 3. person 클래스만 필터링하여 카운트
detections = results[0].boxes  # 감지된 모든 객체의 바운딩 박스
person_count = sum(1 for box in detections if box.cls == 0)  # "person" 클래스 ID는 일반적으로 0

# 안전 상태 결정
if angle < 34.99:
    if person_count <= width:
        status = "\033[92m안전\033[0m"  # 초록색
    elif person_count <= width*1.5:
        status = "\033[93m보통\033[0m"  # 노란색
    else:
        status = "\033[91m위험\033[0m"  # 빨간색
else:
    if person_count <= width*0.7/math.tan(angle):
        status = "\033[92m안전\033[0m"  # 초록색
    elif person_count <= width*1.5*0.7/math.tan(angle):
        status = "\033[93m보통\033[0m"  # 노란색
    else:
        status = "\033[91m위험\033[0m"  # 빨간색

print(f"현재 상태: {status} (감지된 사람 수: {person_count})")

# 좌표 설정
region_points = {
    "region-01": [(764, 364), (816, 416), (516, 464), (778, 622), (100, 361), (140, 270), (260, 261), (376, 394)]
}

# 구역 설정
region = solutions.RegionCounter(
    show=True,
    region=region_points,
    model="./yolov8x.pt"
)

# 결과 이미지 저장
image = results[0].plot()
cv2.imwrite("project/result_obb2.jpg", image)
