FROM python:3.8-slim-buster
LABEL org.opencontainers.image.source=https://github.com/?????????/exercise13
WORKDIR /python-docker
COPY . /python-docker/
RUN pip install -r requirements.txt CMD [ "python", "app.py"]
