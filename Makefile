#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Django
.PHONY: build
build:
	docker-compose -f local.yml build
	docker-compose -f local.yml up

.PHONY: start
start:
	docker-compose -f local.yml up

.PHONY: superuser
superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

.PHONY: migrations
migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations
	docker-compose -f local.yml run --rm django python manage.py migrate

.PHONY: flush
migrations:
	docker-compose -f local.yml run --rm django python manage.py flush

.PHONY: startapp
migrations:
	docker-compose -f local.yml run --rm django python manage.py startapp sars_dashboard/projects
