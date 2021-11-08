FROM python:3.8-slim

RUN pip install opencv-python-headless argh pillow

WORKDIR /app/
COPY main.py /app/main.py
COPY deps/ /deps/

ENV HAAR_PATH=/deps/haarcascade_frontalface_default.xml

CMD python main.py