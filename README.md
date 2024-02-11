# TechStack
To run the docker instance, once the docker server is running:
docker-compose up -d --build

To run after changing the models:
docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade

Frontend package.json Dependencies:
axios, bootstrap, core-js, vue, vue-router, vuex

Backend Docker Requirements:
aerich, asyncpg, bcrypt, passlib, fastapi, python-jose, python-multipart, tortoise-orm, uvicorn
