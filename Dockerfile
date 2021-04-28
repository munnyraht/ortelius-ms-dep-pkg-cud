FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install psycopg2-binary

RUN pip3 install -r requirements.txt

COPY main.py main.py

COPY wsgi.py wsgi.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]