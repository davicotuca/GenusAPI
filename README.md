# GenusAPI
# rodar lint
docker-compose run --rm app sh -c "flake8"
# rodar testes
docker-compose run --rm app sh -c "python manage.py test"