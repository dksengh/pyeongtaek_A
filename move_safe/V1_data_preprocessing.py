import cv2
import glob
import os

#  전처리할 이미지가 있는 폴더 경로
base_folder = "./V9_newproject/datasets/images"  # 'images' 폴더로 경로 수정

#  저장할 폴더 경로 (새로운 폴더 생성)
output_folder = os.path.join(base_folder, "brightened")  # 'brightened'라는 새 폴더

#  밝기 조정 계수 (1.5배 밝게)
ALPHA = 1.5  
BETA = 0    

#  폴더가 존재하지 않으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"📂 '{output_folder}' 폴더가 생성되었습니다.")
else:
    print(f"📂 '{output_folder}' 폴더가 이미 존재합니다.")

# 이미지 경로 가져오기 (대소문자 구분 없이 .jpg와 .JPG 파일 모두 포함)
image_files_train = glob.glob(os.path.join(base_folder, "train", "*.jpg")) + glob.glob(os.path.join(base_folder, "train", "*.JPG"))
image_files_valid = glob.glob(os.path.join(base_folder, "val", "*.jpg")) + glob.glob(os.path.join(base_folder, "val", "*.JPG"))

# 두 경로에서 이미지 파일 리스트 합치기
image_files = image_files_train + image_files_valid


# 이미지 로드 및 밝기 조정 (새 폴더에 저장)
for image_path in image_files:
    # 파일명 추출
    filename = os.path.basename(image_path)
    new_filename = os.path.splitext(filename)[0] + "_brightened.jpg"
    output_path = os.path.join(output_folder, new_filename)

    # 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print(f"⚠️ 이미지 로드 실패: {image_path}")
        continue

    # 밝기 조정
    brightened_img = cv2.convertScaleAbs(img, alpha=ALPHA, beta=BETA)

    # 새 폴더에 저장
    cv2.imwrite(output_path, brightened_img)
    print(f"✅ 저장 완료: {output_path}")

print(f"🎉 총 {len(image_files)}개의 이미지가 밝게 조정되어 '{output_folder}' 폴더에 저장되었습니다.")


