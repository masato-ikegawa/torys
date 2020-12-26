FROM python:3.8

WORKDIR /usr/src

RUN apt-get update && apt-get install -y libgl1-mesa-dev 
RUN apt update && apt install -y nginx

RUN pip install flask flask_cors uwsgi numpy opencv-python