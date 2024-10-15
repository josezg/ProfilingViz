FROM python:3.10 AS base

ENV PYTHONPATH=$PYTHONPATH:/src/

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ /src/

FROM base AS build
CMD streamlit run --server.port 9090 app.py