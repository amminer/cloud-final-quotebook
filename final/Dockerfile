FROM python:3.10-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir && echo "this container is configured to listen on port 8080"

ENTRYPOINT ["python3"]

CMD ["app.py"]
