
FROM python:3.9


WORKDIR /selfsanta-system


COPY ./requirements.txt /selfsanta-system/requirements.txt


RUN pip install -r ./requirements.txt


COPY ./app /selfsanta-system/app


CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
