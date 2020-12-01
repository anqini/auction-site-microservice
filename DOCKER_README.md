docker build -t login_service microservices/login_service/.
docker run --rm login_service nameko run --config config.yaml login

docker build -t login_service microservices/user_service/.
docker run --rm login_service nameko run --config config.yaml user

docker build -t login_service microservices/admin_service/.
docker run --rm login_service nameko run --config config.yaml admin

docker build -t login_service microservices/item_service/.
docker run --rm login_service nameko run --config config.yaml item
