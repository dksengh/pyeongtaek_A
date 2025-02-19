# pip install ultralytics
#  분류 모델 구현 
from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("./runs/detect/train28/weights/best.pt") # ./runs/detect/train28/weights/best.pt ./yolo11n.pt

# 2. 모델 예측
results = model(
    "./filtered_images/frame_2790.jpg"

)

# 3. 이미지 저장
image = results[0].plot()
cv2.imwrite("./result_image3.jpg", image)
