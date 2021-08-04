# Python-Microservices-Web-App
Learning Django and how to build microservices

Deploy production
I. DEPLOY PRODUCTION ADMIN
1. Run docker command
$ docker-compose up
2. sh to workspace:
$ docker-compose exec backend bash

II. DEPLOY PRODUCTION MAIN
1. install library in manager.py file
2. run container
 $ docker-compose up
3. ssh into workspace:
$ docker-compose exec backend bash
- Migration (process inside workspace):
$ python manager.py db init
$ python manager.py db migrate
$ python manager.py db upgrade
