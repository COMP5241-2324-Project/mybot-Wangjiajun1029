FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV REDIS_HOST=redis-server
ENV REDIS_PORT=6379

CMD ["python", "-u", "app.py"]