FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python3"]

CMD ["app.py"]
