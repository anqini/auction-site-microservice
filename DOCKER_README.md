
## How to run microserivce


```
docker build -t api_server -f microservices/api_server/Dockerfile .
docker run -it --rm api_server -p 5000:5000 python3 api.py

docker build -t login_service -f microservices/login_service/Dockerfile .
docker run -it --rm  login_service

docker build -t user_service -f microservices/user_service/Dockerfile .
docker run -it --rm  user_service 

docker build -t admin_service -f microservices/admin_service/Dockerfile .
docker run -it --rm  admin_service

docker build -t search_service -f microservices/search_service/Dockerfile .
docker run -it --rm search_service

docker build -t item_service -f microservices/item_service/Dockerfile .
docker run -it --rm  item_service

docker build -t notification_service -f microservices/notification_service/Dockerfile .
docker run -it --rm notification_service

docker build -t auction_service -f microservices/auction_service/Dockerfile .
docker run -it --rm auction_service
```
