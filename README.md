# Auction Site - Final Project

Final project for MPCS 51205 Aut 2020 from Team White Fifty Fifty 

## Frontend

Tech stack: HTML, CSS, JavaScript, Django, Redis 

### Install
Open `webserver` directory.

Creating and activating virtual environment (Optional)
```
virtualenv venv
source venv/bin/activate
```

Install and start Redis server on Mac
```
brew install redis
redis-server /usr/local/etc/redis.conf
```
* [Linux](https://redis.io/topics/quickstart)
* [Windows](https://www.onlinetutorialspoint.com/spring-boot/setup-install-redis-server-on-windows-10.html)

Navigate back to the `webserver` folder. Install requirements and make migrations
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### NOTE

Django will generate an sqlite database by default, but we are not using it to store any information.

## Backend

### Descrption
Based on python packages: Nameko, Flask, Pymongo, psycopg2, flasgger

### How to run backend microserivce
Please open 8 seperate terminals and type two command in each terminal.

1. api_server
```
docker build -t api_server -f microservices/api_server/Dockerfile .
docker run -it --rm api_server -p 5000:5000 python3 api.py
```

2. login_service
```
docker build -t login_service -f microservices/login_service/Dockerfile .
docker run -it --rm  login_service
```

3. user_service
```
docker build -t user_service -f microservices/user_service/Dockerfile .
docker run -it --rm  user_service 
```

4. admin_service
```
docker build -t admin_service -f microservices/admin_service/Dockerfile .
docker run -it --rm  admin_service
```

5. search_service
```
docker build -t search_service -f microservices/search_service/Dockerfile .
docker run -it --rm search_service
```

6. item_service
```
docker build -t item_service -f microservices/item_service/Dockerfile .
docker run -it --rm  item_service
```

7. notification_service
```
docker build -t notification_service -f microservices/notification_service/Dockerfile .
docker run -it --rm notification_service
```

8. auction_service
```
docker build -t auction_service -f microservices/auction_service/Dockerfile .
docker run -it --rm auction_service
```
