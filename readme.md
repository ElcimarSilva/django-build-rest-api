## Repositorio para armazenar informações sobre o curso de python com django Build a Backend REST API with Python & Django - Advanced da Udemy

## Tecnologias
- Python
- Django
- Postgres
- Swagger
- Docker
- Github

## configs
- criado um access token no docker hub e inserido como secret do projeto no github
-- https://hub.docker.com/

## rodar o docker para ler o Dockerfile e realizar a criação
- docker build .
- docker compose build
- sudo docker compose run --rm app sh -c  "django-admin startproject app ."
- docker compose up
## flake8
- docker compose run --rm app sh -c "flake8"

## Test
- docker compose run --rm app sh -c "python manage.py test"
- docker compose run --rm app sh -c "python manage.py startapp core"