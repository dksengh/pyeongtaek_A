import cv2
import os
# import cv2.dnn_superres as dnn_superres

# 영상 파일 경로 설정
video_path = "./V9_newproject/2025-02-03 17-02-04.mp4"
output_folder = "frames_upscaled"  # 화질 개선된 이미지 저장 폴더

# 저장 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# OpenCV로 영상 불러오기
cap = cv2.VideoCapture(video_path)

# FPS 가져오기
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 초당 프레임 수
frame_interval = fps // 25  # 25FPS마다 한 장 저장

frame_count = 0
image_count = 0

# Super-Resolution 모델 로드
# sr = dnn_superres.DnnSuperResImpl_create()
# sr_model_path = "EDSR_x2.pb"  # 사용할 모델 파일 (EDSR 모델 예제)
# sr.readModel(sr_model_path)
# sr.setModel("edsr", 2)  # 모델 타입과 업스케일 비율 설정 (2배 업스케일)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 영상 끝나면 종료

    # 지정한 프레임 간격마다 저장
    if frame_count % frame_interval == 0:
        # 초해상도 적용
        # upscaled_frame = sr.upsample(frame)

        img_name = f"{output_folder}/frame_{image_count:04d}.jpg"
        cv2.imwrite(img_name, )  #  cv2.imwrite(img_name, upscaled_frame)
        print(f"Saved: {img_name}")

        image_count += 25

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
