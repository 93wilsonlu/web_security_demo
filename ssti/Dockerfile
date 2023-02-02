FROM python:3.11

WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y iputils-ping
RUN pip3 install flask

RUN adduser --system --no-create-home app
USER app

CMD ["python3", "app.py"]