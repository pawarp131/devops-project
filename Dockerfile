FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
ENV APP_VERSION=1.0
ENV ENV=production
CMD ["python", "app.py"]
