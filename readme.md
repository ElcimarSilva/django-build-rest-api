## Repositorio para armazenar informações sobre o curso de python com django Build a Backend REST API with Python & Django - Advanced da Udemy

## Tecnologias
- Python
- Django
- Postgres
- Swagger
- Docker
- Github

## Configs
- criado um access token no docker hub e inserido como secret do projeto no github
-- https://hub.docker.com/

## Codar o docker para ler o Dockerfile e realizar a criação
- docker build .
- docker compose build
- sudo docker compose run --rm app sh -c  "django-admin startproject app ."
- docker compose up
- docker-compose -f docker-compose-deploy.yml up
## Flake8
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


#TODO: verificar conta na aws free tier não esta mais disponivel
#TODO: verificar actions que estão rodando no git e quebrando os testes
#TODO: verificar porque não consegui abrir a URL quando executo o comando docker-compose -f docker-compose-deploy.yml up
#TODO: realizar mais testes na api criada e explorar mais e como modificala para outros casos

metricas de api:
- requisições por segundo
- tempo de reposta
- usuarios online
- taxa de erros
- total de requests