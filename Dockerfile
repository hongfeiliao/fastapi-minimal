FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
COPY app ./app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "-m", "fastapi", "run", "app/main.py" ]
