## 평택대학교 OO팀 프로젝트
```
YOLO를 활용한 평지 및 경사로에서의 실시간 유동 인구 감지와 안전 수용 인원 계산
```
## 구성원
```
팀원: 박성현, 서대환, 배준서, 김보민
```
## 설명
```
군중 이동 시 안전한 수용 인원 계산 및 위험 알림 기능

군중들이 이동할 때, 1㎡당 2명을 초과하면 이동 속도가 급격히 감소하고 사고 위험이 증가합니다.
평지에서 안전한 이동을 위해서는 1㎡당 1~2명의 사람들이 있을 때가 적절하다고 합니다.
이 기준을 바탕으로, 경사로에서도 안전한 수용 인원 수를 계산할 수 있습니다.
경사로에서는 경사각에 따라 미끄러짐 위험이 커지므로, 이를 고려한 안전 수용 인원 계산식은 다음과 같습니다:
(콘크리트 바닥과 고무 밑창 신발의 마찰계수는 0.7이다.)

```
```math
\text{수용 인원} = \text{면적} \times (1or2) \times \frac{0.7}{\tan(\theta)}
```
```

이 식은 경사각에 따른 안전한 인원 수를 계산하는 데 사용됩니다.
이 계산식을 통해, 공간에 수용할 수 있는 안전한 인원 수를 실시간으로 모니터링하고, 수용 인원이 넘었을 때 위험을 알리는 기능을 구현할 수 있습니다.
이 기능은 군중 밀집 상태를 감지하여, 사고를 예방하고 안전한 이동 환경을 제공하는 데 도움을 줍니다
```
## 예상 목차
1. 데이터 수집
<img width="563" alt="Dublin, Ireland" src="https://github.com/user-attachments/assets/06494445-6a93-44d2-9043-cfbc5b9d62b7" />
<img width="363" alt="Dublin, Ireland 면적" src="https://github.com/user-attachments/assets/91c57030-5785-4f67-b27e-bca2d1527e8e" />

구글링을 통해 기존에 ai학습을 위해 사용했었던 데이터들을 수집하였고, 유튜브에서 거리 라이브영상을 추가로 추출하여 훈련하였다.

2. 데이터 라벨링
<br> LabelImg 프로그램으로 yolo를 이용해 객제 person을 라벨링하였다.

3. 데이터 전처리

4. 모델 학습

5. 모델 평가

6. 모델 적용

7. 인파 밀집 시스템 로직 구현

8. 웹서비스

9. 알림 설정

10. ppt자료 준비

11. 깃허브 소스 코드 관리

## 참고자료
```
https://drive.google.com/drive/folders/1O9VNYJGcSItNEewLlcGSf3v71nDdDE4_?usp=drive_link

https://kiss-kstudy-com.libproxy.ptu.ac.kr/Detail/Ar?key=4059409 // 보행자 깊이 정보를 이용한 군중 밀집도 추정 논문
https://www-dbpia-co-kr.libproxy.ptu.ac.kr/journal/articleDetail?nodeId=NODE11917835 // 군중 밀집도 인식을 위한 알고리즘 비교 연구 논문
https://www-dbpia-co-kr.libproxy.ptu.ac.kr/journal/articleDetail?nodeId=NODE12014061 // 도심 군중밀집 안전을 위한 인공지능 기반의 영상분석 시스템 개발 논문
```

