FROM python:3.14-slim

RUN adduser --disabled-password --gecos '' appuser
WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping curl && apt-get clean
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN chown -R appuser:appuser /app
USER appuser

RUN pip install --no-cache-dir --no-warn-script-location -r requirements.txt


CMD ["python", "main.py"]
