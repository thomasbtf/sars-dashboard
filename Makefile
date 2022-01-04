#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Django
.PHONY: build
build:
	docker-compose -f local.yml build

.PHONY: start
start:
	docker-compose -f local.yml up

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
	docker-compose -f local.yml run --rm django python manage.py flush
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -rf sars_dashboard/media

.PHONY: app
app:
	docker-compose -f local.yml run --rm django python manage.py startapp $(name)
