
FROM python:3.9


WORKDIR /selfsanta-system


COPY ./requirements.txt /selfsanta-system/requirements.txt


RUN pip install -r ./requirements.txt


COPY ./app /selfsanta-system/app

CMD ["gunicorn", "-w", "6", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]

# CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
