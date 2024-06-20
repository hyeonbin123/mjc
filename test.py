from ultralytics import YOLO
from pathlib import Path
import matplotlib.pyplot as plt
import cv2

# YOLOv8 모델 로드
model = YOLO('trained_model_coco.pt')

# 이미지 경로
image_path = 'test1.jpg'

# 이미지 로드
img = cv2.imread(image_path)

# YOLOv8 모델을 사용하여 객체 검출
results = model(img)

# 결과를 처리하여 출력
print(results)  # 터미널에 결과 출력

# 결과 이미지 저장
save_dir = Path('runs/detect/exp')
save_dir.mkdir(parents=True, exist_ok=True)
output_image_path = save_dir / Path(image_path).name

# YOLOv8 결과를 이미지에 그리기
annotated_img = results[0].plot()

# 결과 이미지 저장
cv2.imwrite(str(output_image_path), annotated_img)

# 결과 이미지 보여주기
output_img = cv2.imread(str(output_image_path))

plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
