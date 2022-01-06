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
	docker-compose -f local.yml run --rm django python manage.py flush
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -rf sars_dashboard/media

.PHONY: app
app:
	docker-compose -f local.yml run --rm django python manage.py startapp $(name)

#* Django Production
.PHONY: production-build
production-build:
	docker-compose -f production.yml build

.PHONY: production-start
production-start:
	docker-compose -f production.yml up

.PHONY: production-startd
production-startd:
	docker-compose -f production.yml up -d

.PHONY: production-superuser
production-superuser:
	docker-compose -f production.yml run --rm django python manage.py createsuperuser

.PHONY: production-migrations
production-migrations:
	docker-compose -f production.yml run --rm django python manage.py migrate

.PHONY: production-shell
production-shell:
	docker-compose -f production.yml run --rm django python manage.py shell
