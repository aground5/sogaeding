FROM python:3.8.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /

# entrypoint.sh 파일 권한 변경
RUN sed -i 's/\r//' /korea.sh
RUN chmod +x /korea.sh
RUN sed -i 's/\r//' /setup.sh
RUN chmod +x /setup.sh
RUN /setup.sh
# running entrypoint
ENTRYPOINT ["/korea.sh"]
