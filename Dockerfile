FROM python:3.10-bullseye

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN \
    pip install --upgrade pip \
    && pip install -r requirements.txt


RUN mkdir /app
COPY ./app /app
WORKDIR /app

EXPOSE 8010
CMD ["bash"]
