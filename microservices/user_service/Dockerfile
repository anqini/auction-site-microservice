FROM mongo
# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7-dev

WORKDIR /src
COPY . .
RUN python3 -m pip install --upgrade pip 
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install psycopg2-binary

WORKDIR /src/service
CMD mongod & python3 ../db/create_mongo_dbs.py;\
    python3 ../db/isolate_user_service.py;\
    nameko run --config config.yaml user
