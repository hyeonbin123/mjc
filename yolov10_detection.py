from ultralytics import YOLOv10

# YOLOv10 모델 로드
model = YOLOv10('yolov10x.pt')

def detect_objects(image_path):
    results = model(image_path)
    class_names = model.names  # 모델의 클래스 이름 목록
    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # 탐지된 객체의 좌표 및 클래스 정보 추출
            xmin, ymin, xmax, ymax = box.xyxy[0].tolist()
            conf = box.conf[0].item()
            cls = box.cls[0].item()
            class_name = class_names[int(cls)]  # 클래스 ID를 이름으로 변환
            res = {"ClassName":class_name,"Confidence":conf, "Box":(xmin, ymin, xmax, ymax)}
            detections.append(res)
            # detections.append(f"Class: {class_name}, Confidence: {conf:.2f}, Box: ({xmin:.2f}, {ymin:.2f}, {xmax:.2f}, {ymax:.2f})")
    return detections
