# Simple Dockerfile for Flask app
FROM python:3.10-slim
WORKDIR /app
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
