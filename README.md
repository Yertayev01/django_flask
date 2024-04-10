pip install django, djangorestframework
django-admin startproject "project-name"
cd admin
python manage.py runserver
create requirements.txt, Dockerfile, docker-compose.yml files


docker-compose exec backend sh
python manager.py db init
python manager.py db migrate

...


cd admin docker-compose exec backend sh