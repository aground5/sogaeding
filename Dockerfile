FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# entrypoint.sh 파일 권한 변경
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh
# running entrypoint
ENTRYPOINT ["/entrypoint.sh"]
