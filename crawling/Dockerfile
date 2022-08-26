FROM python:3.9

WORKDIR /
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./setup.sh /
RUN apt update
RUN apt install -y libmecab-dev

RUN sed -i 's/\r//' /setup.sh
RUN chmod +x /setup.sh
RUN /setup.sh

RUN wget https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh
RUN chmod +x /mecab.sh
RUN /mecab.sh

COPY . /
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# entrypoint.sh 파일 권한 변경
RUN sed -i 's/\r//' /korea.sh
RUN chmod +x /korea.sh
RUN sed -i 's/\r//' /america.sh
RUN chmod +x /america.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
# running entrypoint
ENTRYPOINT ["/start.sh"]
