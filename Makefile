lock:
	pipenv lock

install:
	pipenv install

build:
	docker build -t docker-sercure-containers-api .

run: build
	docker run -p 5000:5000 docker-sercure-containers-api:latest
	docker logs --follow docker-sercure-containers-api
