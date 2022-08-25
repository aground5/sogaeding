FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./common /common
COPY ./config /config
COPY ./earth_diary /earth_diary
COPY ./static /static
COPY ./templates /templates
COPY ./.env /.env
COPY ./entrypoint.sh /entrypoint.sh
COPY ./gunicorn-cfg.py /gunicorn-cfg.py
COPY ./manage.py /manage.py
COPY ./requirements.txt /requirements.txt
COPY ./secrets.json /secrets.json

# entrypoint.sh 파일 권한 변경
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
# running entrypoint
ENTRYPOINT ["/entrypoint.sh"]
