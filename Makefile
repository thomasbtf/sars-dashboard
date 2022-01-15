#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Django Local
.PHONY: l-build
l-build:
	docker-compose -f docker-compose-local.yml build
	docker-compose -f docker-compose-local.yml run --rm django python manage.py migrate

.PHONY: l-build-start
l-build-start:
	make l-flush
	docker-compose -f docker-compose-local.yml build
	docker-compose -f docker-compose-local.yml run --rm django python manage.py migrate
	make l-superuser
	docker-compose -f docker-compose-local.yml up

.PHONY: l-start
l-start:
	docker-compose -f docker-compose-local.yml up

.PHONY: l-startd
l-startd:
	docker-compose -f docker-compose-local.yml up -d

.PHONY: l-superuser
l-superuser:
	docker-compose -f docker-compose-local.yml run --rm django python manage.py createsuperuser

.PHONY: makemigrations
l-makemigrations:
	docker-compose -f docker-compose-local.yml run --rm django python manage.py makemigrations $(app)

.PHONY: l-migrations
l-migrations:
	docker-compose -f docker-compose-local.yml run --rm django python manage.py makemigrations $(app)
	docker-compose -f docker-compose-local.yml run --rm django python manage.py migrate

.PHONY: flush
l-flush:
	docker rm -f django
	docker rm -f celeryworker
	docker rm -f celerybeat
	docker rm -f flower
	docker rm -f postgres
	docker rm -f sars-dashboard_redis_1
	docker rm -f mailhog
	docker volume rm -f sars-dashboard_local_postgres_data
	docker volume rm -f sars-dashboard_local_postgres_data_backups
	docker volume rm -f sars-dashboard_local_redis

.PHONY: rmv-migrations
rmv-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	rm -rf sars_dashboard/media

.PHONY: app
app:
	docker-compose -f docker-compose-local.yml run --rm django python manage.py startapp $(name)

#* Django Production
.PHONY: p-build
p-build:
	docker-compose -f docker-compose-production.yml build
	docker-compose -f docker-compose-production.yml run --rm django python manage.py migrate

.PHONY: p-start
p-start:
	docker-compose -f docker-compose-production.yml up

.PHONY: p-startd
p-startd:
	docker-compose -f docker-compose-production.yml up -d

.PHONY: p-superuser
p-superuser:
	docker-compose -f docker-compose-production.yml run --rm django python manage.py createsuperuser

.PHONY: p-build-start
p-build-start:
	make p-flush
	make p-build
	make p-superuser
	make p-start

.PHONY: p-build-startd
p-build-startd:
	make p-flush
	make p-build
	make p-superuser
	make p-startd

.PHONY: p-shell
p-shell:
	docker-compose -f docker-compose-production.yml run --rm django python manage.py shell

.PHONY: p-flush
p-flush:
	docker rm -f sars-dashboard_nginx_1
	docker rm -f sars-dashboard_flower_1
	docker rm -f sars-dashboard_celerybeat_1
	docker rm -f sars-dashboard_django_1
	docker rm -f sars-dashboard_celeryworker_1
	docker rm -f sars-dashboard_redis_1
	docker rm -f sars-dashboard_postgres_1
	docker volume rm -f sars-dashboard_production_data
	docker volume rm -f sars-dashboard_production_postgres_data
	docker volume rm -f sars-dashboard_production_postgres_data_backups
	docker volume rm -f sars-dashboard_production_static
	docker volume rm -f sars-dashboard_production_redis

#* K8

.PHONY: kompose
kompose:
	eval $(minikube docker-env)
	make p-build
	kompose convert -f docker-compose-production.yml -o kubernetes-production.yml --build local -v --push-image=false --controller deployment


.PHONY: k-apply
k-apply:
	kubectl apply -f kubernetes-production.yml

.PHONY: k-delete
k-delete:
	kubectl delete -f kubernetes-production.yml

.PHONY: k-service
k-service:
	minikube service nginx

.PHONY: k-service
k-service:
	minikube service nginx

.PHONY: k-migrate
k-migrate:
	kubectl exec -ti $$(kubectl get pods -l="io.kompose.service=django" -o jsonpath="{.items[0].metadata.name}") -- python manage.py migrate

.PHONY: k-superuser
k-superuser:
	kubectl exec -ti $$(kubectl get pods -l="io.kompose.service=django" -o jsonpath="{.items[0].metadata.name}") -- python manage.py createsuperuser

.PHONY: k8
k8:
	make kompose
	make k-apply
	make k-superuser
	make k-service

.PHONY: restart-minikube
restart-minikube:
	minikube delete --all --purge
	minikube start
