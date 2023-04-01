FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /ecomio-be

COPY . .

RUN pip install -r requirements.txt

VOLUME /ecomio-be

EXPOSE 8080

RUN pwd

CMD python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py runserver 0.0.0.0:8080