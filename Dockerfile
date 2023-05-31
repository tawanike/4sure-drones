FROM python:3.9.14

WORKDIR /app

RUN mkdir -p ~/static

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc zlib1g-dev git && \
    apt-get install -y build-essential python-dev

ADD . .

RUN pip3 install -r requirements.txt

RUN python3 manage.py collectstatic --noinput

RUN python3 manage.py migrate

RUN python3 manage.py initadmin

RUN python3 manage.py loaddata drones.json medication.json


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
