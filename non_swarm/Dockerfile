FROM python:3.4-alpine

LABEL MAINTAINER="shambhu.shrestha@gmail.com"
ADD ./code /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "hello.py"]