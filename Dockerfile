# base image
FROM python:3.11

# setup environment variable
ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# use a different mirror and install ffmpeg with retries
RUN apt-get update -o Acquire::Retries=3 -o Acquire::http::Timeout="60" && \
    apt-get install -y ffmpeg

# copy whole project to your docker home directory.
COPY . $DockerHOME

# run this command to install all dependencies
RUN pip install -r src/requirements/dev.txt

# port where the Django app runs
EXPOSE 8000

# start server
CMD python src/manage.py runserver 0.0.0.0:8000
