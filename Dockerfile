FROM jupyter/datascience-notebook

USER root

# Needed to build cryptography package
RUN apt-get update && apt-get install -y build-essential libgmp3-dev python3-dev

ADD . /opt/pepsi

WORKDIR /opt/pepsi

RUN pip install virtualenv

RUN cd /opt/pepsi && virtualenv env && env/bin/python setup.py develop

EXPOSE 8000
