FROM python:3.8-slim

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY service service
COPY data data

CMD python -m service
