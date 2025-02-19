from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 1.Yolo 모델 로드
model = YOLO("./yolo11n.pt")

# 2. 모델 훈련
model.train(
    data = "./V9_newproject/detectperson.yaml",
    epochs = 10,
    device="cpu"
)
