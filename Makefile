#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Django Local
.PHONY: build
build:
	docker-compose -f local.yml build

.PHONY: start
start:
	docker-compose -f local.yml up

.PHONY: startd
startd:
	docker-compose -f local.yml up -d

.PHONY: superuser
superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

.PHONY: makemigrations
makemigrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations $(app)

.PHONY: migrations
migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations $(app)
	docker-compose -f local.yml run --rm django python manage.py migrate

.PHONY: flush
flush:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -rf sars_dashboard/media
	docker rm -f sars_dashboard_local_celeryworker
	docker rm -f sars_dashboard_local_flower
	docker rm -f sars_dashboard_local_django
	docker rm -f sars_dashboard_local_celerybeat
	docker rm -f sars_dashboard_production_postgres
	docker rm -f mailhog/mailhog:v1.0.0
	docker volume rm -f sars-dashboard_local_postgres_data
	docker volume rm -f sars-dashboard_local_postgres_data_backups

.PHONY: app
app:
	docker-compose -f local.yml run --rm django python manage.py startapp $(name)

#* Django Production
.PHONY: p-build
p-build:
	docker-compose -f production.yml build
	docker-compose -f production.yml run --rm django python manage.py migrate

.PHONY: p-build-start
p-build-start:
	docker-compose -f production.yml build
	docker-compose -f production.yml run --rm django python manage.py migrate
	docker-compose -f production.yml up

.PHONY: p-start
p-start:
	docker-compose -f production.yml up

.PHONY: p-startd
p-startd:
	docker-compose -f production.yml up -d

.PHONY: p-superuser
p-superuser:
	docker-compose -f production.yml run --rm django python manage.py createsuperuser

.PHONY: p-migrations
p-migrations:
	docker-compose -f production.yml run --rm django python manage.py migrate

.PHONY: p-shell
p-shell:
	docker-compose -f production.yml run --rm django python manage.py shell

.PHONY: p-flush
p-flush:
	docker rm -f sars-dashboard_nginx_1
	docker rm -f sars-dashboard_flower_1
	docker rm -f sars-dashboard_celerybeat_1
	docker rm -f sars-dashboard_django_1
	docker rm -f sars-dashboard_celeryworker_1
	docker rm -f sars-dashboard_redis_1
	docker rm -f sars-dashboard_postgres_1
	docker volume rm -f sars-dashboard_production_media
	docker volume rm -f sars-dashboard_production_postgres_data
	docker volume rm -f sars-dashboard_production_postgres_data_backups
	docker volume rm -f sars-dashboard_production_static
