FROM python:3.9

RUN mkdir /route_builder

WORKDIR /route_builder

RUN pip install gunicorn==21.2.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]