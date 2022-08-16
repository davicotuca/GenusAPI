FROM python:3.9-alpine3.13
LABEL maintainer="Davi Oliveira, Natassha Yukari, GianLuca Almeida"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# O & \ é usada para juntar varios comandos no mesmo run, se rodar cada camada com um run cria um layer cada vez, deixando a imagem mais pesada
# cria um ambient virtual
# faz o update do packge management
# instala os requisitos
# remove as dependencias adicionais que podem ter sido criadas, ou dependencias temporarias, que devem ser adicionadas nessa pasta
# adiciona um novo user, para não usar o root, por segurança

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# define o path como variavel, que é onde os comandos irão rodar
ENV PATH="/py/bin:$PATH"

# define esse usario como usuario padrão
USER django-user