FROM python:3.8-slim

RUN pip install pytz argh

WORKDIR /app/
COPY main.py /app/main.py

CMD python main.py