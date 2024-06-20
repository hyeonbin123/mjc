import sys
import os
import streamlit as st
from yolov10_detection import detect_objects
from text_generation import generate_text
from PIL import Image
import tempfile

# 모듈 경로 추가
sys.path.append(r"C:/Users/jhb04/바탕 화면/school")

st.title("이미지 업로드 및 객체 탐지")
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # 임시 파일 생성
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image_path = temp_file.name
        image.save(image_path)

    # 객체 탐지 수행
    results = detect_objects(image_path)

    # 탐지 결과에서 객체 정보 추출 (중복 제거)
    detected_objects = {}
    for result in results:
        class_name = result['ClassName']
        bbox = result['Box']

        if len(bbox) == 4:
            if class_name not in detected_objects:
                detected_objects[class_name] = bbox

    # 각 탐지된 객체를 잘라내고 설명 생성
    for name, bbox in detected_objects.items():
        
        # bbox 값 변환 및 객체 이미지 잘라내기
        xmin, ymin, xmax, ymax = map(float, bbox)
        cropped_image = image.crop((xmin, ymin, xmax, ymax))

        # 컬럼 생성 (왼쪽: 객체 이미지, 오른쪽: 설명)
        col1, col2 = st.columns(2)

        with col1:
            st.image(cropped_image, use_column_width=True)

        with col2:
            description = generate_text(f"{name}에 대한 설명을 한국어로 간단하게 작성해 주세요.")
            st.write(f"{name}에 대한 설명: {description}")
    
    # 임시 파일 삭제
    os.remove(image_path)
