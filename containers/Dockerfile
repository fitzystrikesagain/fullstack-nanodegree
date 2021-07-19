FROM python:3.7.2-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
& pip install flask

ENTRYPOINT ["python", "app.py"]
