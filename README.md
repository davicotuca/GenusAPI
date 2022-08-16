# GenusAPI
# para iniciar
# rodar na primeira vez
docker-compose build
docker-compose up

# usada para criar o core
docker-compose run --rm app sh -c "python manage.py startapp core"

# rodar lint
docker-compose run --rm app sh -c "flake8"
# rodar testes
docker-compose run --rm app sh -c "python manage.py test"