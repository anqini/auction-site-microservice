FROM python:3.9
RUN apt-get update
WORKDIR /src
COPY . .
RUN python3 -m pip install --upgrade pip 
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install psycopg2-binary
WORKDIR /src/service

CMD nameko run --config config.yaml login
