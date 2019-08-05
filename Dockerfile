FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD uwsgi --socket 0.0.0.0:5000 --protocol=http --module app:app
