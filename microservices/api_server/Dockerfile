FROM python:3.9
RUN apt-get update
WORKDIR /src
COPY . .
RUN python3 -m pip install --upgrade pip 
RUN python3 -m pip install -r requirements.txt
WORKDIR /src/app
EXPOSE 5000