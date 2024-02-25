# What the project is
A full-stack Create, Read, Update, Delete(CRUD) message board application, where visitors can do CRUD operations on accounts and messages.

# How to run it
To run the docker instance, once the docker server is running:

cd fastapi-vue

docker-compose up -d --build

Then visit: http://localhost:8080/

To run after changing the models:

docker-compose exec backend aerich migrate

docker-compose exec backend aerich upgrade

# General Technologies

FastAPI, Vue, Docker and PostgreSQL

# All Dependencies/Requirements
Frontend package.json Dependencies:

axios, bootstrap, core-js, vue, vue-router, vuex

Backend Docker Requirements:

aerich, asyncpg, bcrypt, passlib, Fastapi, python-jose, python-multipart, tortoise-orm, uvicorn
