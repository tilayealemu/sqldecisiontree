###############################################
# Dockerfile to build python and scikit-learn #
#               Based on Ubuntu               #
###############################################
FROM ubuntu:16.04

MAINTAINER Tilaye ALemu tilaye@gmail.com

RUN apt-get update
RUN apt-get -y install build-essential python-dev python-setuptools python-pip
RUN apt-get -y install python-numpy python-scipy libatlas-dev libatlas3-base
RUN pip install flask flask-restful
RUN pip install -U pandas scikit-learn
COPY out/sample /root/sample
COPY out/dtsql.py /root/
RUN touch /var/tmp/dtsql.forever

WORKDIR /root

CMD tail -f /var/tmp/dtsql.forever

EXPOSE 3306
