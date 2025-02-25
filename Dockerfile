# python 3.11.5버전 이미지를 사용해 빌드 - 프로젝트 파이썬 버전
FROM python:3.11.5

# .pyc 파일을 생성하지 않도록 설정합니다.
ENV PYTHONDONTWRITEBYTECODE 1

# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하도록 설정합니다.
ENV PYTHONUNBUFFERED 1

# /app/ 디렉토리를 생성합니다.
RUN mkdir /app/

# /app/ 경로를 작업 디렉토리로 설정합니다.
WORKDIR /app/

# requirments.txt를 작업 디렉토리(/app/) 경로로 복사
# Dockerfile은 프로젝트를 클론 받아온 mylog 디렉토리에 존재.
COPY requirements.txt .

# 프로젝트 실행에 필요한 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# gunicorn을 사용하기 위한 패키지를 설치합니다.
RUN pip install gunicorn psycopg2