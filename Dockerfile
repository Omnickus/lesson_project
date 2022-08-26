from python:3.10-alpine

WORKDIR /mpp

COPY requarements.txt ./

RUN pip install -U pip
RUN pip install -r requarements.txt
RUN mkdir screenshot

COPY ./ ./





