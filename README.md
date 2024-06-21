### README.md

# 이미지 업로드 및 객체 탐지 기반의 설명 제공 웹 애플리케이션 개발

## 개요
이 프로젝트는 사용자로 하여금 이미지를 업로드하고, 업로드된 이미지에서 객체를 탐지하여 해당 객체에 대한 설명을 제공하는 웹 애플리케이션을 개발하는 것을 목표로 합니다. 이를 위해 YOLOv10 모델을 사용하여 객체를 탐지하고, Hugging Face의 텍스트 생성 모델을 사용하여 탐지된 객체에 대한 설명을 생성합니다.

## 주요 기능
- **이미지 업로드:** 사용자는 Streamlit 인터페이스를 통해 이미지를 업로드할 수 있습니다.
- **객체 탐지:** 업로드된 이미지는 YOLOv10 모델을 통해 객체가 탐지됩니다.
- **텍스트 생성:** 탐지된 객체에 대한 정보는 Hugging Face의 텍스트 생성 모델을 통해 설명으로 제공됩니다.

## 설치 방법
이 프로젝트를 로컬에서 실행하려면 다음 단계를 따르십시오.

1. **클론 리포지토리**
    ```sh
    git clone https://github.com/hyeonbin123/mjc.git
    cd mjc
    ```

2. **필수 라이브러리 설치**
    ```sh
    pip install -r requirements.txt
    ```

3. **Streamlit 실행**
    ```sh
    streamlit run app.py
    ```

## 사용된 기술
- **Python:** 개발 언어
- **Streamlit:** 웹 애플리케이션 프레임워크
- **YOLOv10:** 객체 탐지 모델 ([GitHub 링크](https://github.com/THU-MIG/yolov10))
- **Hugging Face Transformers:** 텍스트 생성 모델 ([Hugging Face 링크](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B))

## 파일 설명
- `app.py`: 웹 애플리케이션의 메인 파일로, Streamlit을 사용하여 사용자 인터페이스를 구성하고, 이미지를 업로드 받고, 객체 탐지 및 텍스트 생성을 처리합니다.
- `requirements.txt`: 필요한 라이브러리 목록
- `yolov10_detection.py`: YOLOv10 모델을 사용하여 객체 탐지를 수행하는 코드
- `text_generation.py`: Hugging Face 모델을 사용하여 텍스트 생성을 수행하는 코드


## 사용 방법
1. 웹 애플리케이션을 실행하면, 사용자는 이미지 업로드 버튼을 통해 이미지를 업로드할 수 있습니다.
2. 업로드된 이미지는 YOLOv10 모델을 통해 객체가 탐지됩니다.
3. 탐지된 객체는 Hugging Face의 텍스트 생성 모델을 통해 설명이 생성됩니다.
4. 생성된 설명은 웹 애플리케이션을 통해 사용자에게 제공됩니다.
