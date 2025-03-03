import cv2
import os
import tkinter as tk
import math
import numpy as np
from tkinter import simpledialog
from ultralytics import YOLO, solutions

# 한글 폰트 설정 (Windows의 경우 'malgun.ttf', Mac의 경우 'AppleGothic', Linux의 경우 'NanumGothic')
from PIL import ImageFont, ImageDraw, Image
font_path = "malgun.ttf"  # 시스템 환경에 맞게 변경
font = ImageFont.truetype(font_path, 30)

# YOLO 모델 로드
model = YOLO("yolov8n.pt") # ./runs/detect/train28/weights/best.pt

# GUI 창을 통해 사용자 입력 받기
def get_inputs():
    root = tk.Tk()
    root.title("입력 창")
    root.geometry("300x150")
    
    tk.Label(root, text="넓이㎡:").grid(row=0, column=0)
    # tk.Label(root, text="기울기:").grid(row=1, column=0)
    
    width_entry = tk.Entry(root)
    width_entry.grid(row=0, column=1)
    
    def submit():
        global width
        width = float(width_entry.get())
        root.destroy()
    
    tk.Button(root, text="확인", command=submit).grid(row=2, columnspan=2)
    root.mainloop()

# 사용자 입력 받기
width = 0
get_inputs()

# 입력값 출력
print(f"입력된 값 - 넓이: {width}") # , 기울기: {angle}"

# 분석할 영상 파일 설정
video_path = os.path.expanduser("V9_newproject\EarthCam Live- Dublin, Ireland_test.mp4")

# 전체 영상을 분석하도록 수정
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("비디오 파일을 열 수 없습니다. 경로를 확인하세요.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 모델 예측 수행
        results = model(frame)
        
        def filter_person(results):
            """ person (class 0)만 필터링 """
            person = []
            for result in results:
                for box in result.boxes:
                    if int(box.cls) == 0:  # class 0: person
                        person.append(box.xyxy.tolist()[0])
            return person
        
        # person만 추출
        person_boxes = filter_person(results)
        
        # 감지된 person 객체 수
        person_count = len(person_boxes)
        
        # 안전 상태 결정
        if person_count <= width:
                status = "안전"
                color = (0, 255, 0)  # 초록색
        elif person_count > width and person_count <= width*1.5:
                status = "보통"
                color = (0, 255, 255)  # 노란색
        else:
                status = "위험"
                color = (0, 0, 255)  # 빨간색
        # else:
        #     if person_count <= width*0.7/math.tan(angle):
        #         status = "안전"
        #         color = (0, 255, 0)  # 초록색
        #     elif person_count >= width*0.7/math.tan(angle) and person_count <= width*1.5*0.7/math.tan(angle):
        #         status = "보통"
        #         color = (0, 255, 255)  # 노란색
        #     else:
        #         status = "위험"
        #         color = (0, 0, 255)  # 빨간색
        
        print(f"현재 상태: {status} (감지된 사람 수: {person_count})")
        
        # 결과 영상 출력
        frame = results[0].plot()
        
        # OpenCV 프레임을 PIL 이미지로 변환하여 한글 표시
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(frame_pil)
        draw.text((50, 50), f"{status}", font=font, fill=(0, 255, 0) if status == "안전" else (0, 255, 255) if status == "보통" else (255, 0, 0))
        draw.text((50, 100), f"감지된 사람 수: {person_count}", font=font, fill=(255, 255, 255))
        
        # 다시 OpenCV 형식으로 변환
        frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
        
        # 영상 크기 조절
        frame = cv2.resize(frame, (1120, 630))
        
        cv2.imshow("YOLO Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# 전체 영상 분석 실행
process_video(video_path)