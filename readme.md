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
- docker compose run --rm app sh -c "python manage.py wait_for_db && flake8"
## Test
- docker compose run --rm app sh -c "python manage.py test"

## Criação de novo app
- docker compose run --rm app sh -c "python manage.py startapp example"

## Chamar arquivo ou função especifica(exemplo)
- docker compose run --rm app sh -c "python manage.py wait_for_db"

## Migrations
- python manage.py makemigrations
- python manage.py migrate
- docker compose run --rm app sh -c "python manage.py makemigrations"

# Create a superuser
- docker compose run --rm app sh -c "python manage.py createsuperuser"
- admin@example.com
- 123

# Se autenticar no swagger
- após ter um usuario com email e senha
- chamar endpoint de criação de token
- após ter o token colocar em "authorize" no swagger conforme o exemplo "Token 637ef711224e200b3befdfd0477daeb8c477c00b"


# Perguntas
 - Diferenças entre APIview and viewsets
