FROM python:3.10

WORKDIR /app
COPY . /app
RUN pip3 install flask

RUN adduser --system --no-create-home app
USER app

CMD ["python3", "app.py"]