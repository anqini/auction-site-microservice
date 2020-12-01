FROM base_server
WORKDIR /src/Final-Project/service
RUN mongod & python3 ../db/create_mongo_dbs.py 
RUN mongod & python3 ../db/isolate_admin_service.py 
