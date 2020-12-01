FROM base_server
WORKDIR /src/Final-Project/service
RUN service postgresql start
RUN python3 ../db/create_postgres_dbs.py 
RUN python3 ../db/isolate_item_service.py 
