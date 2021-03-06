# Sequencing Dashboard

[![Tests](https://github.com/thomasbtf/sars-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/thomasbtf/sars-dashboard/actions/workflows/ci.yml)

Dashboard to browse analyses created by UnCoVar.

## Getting Up and Running Locally With Docker

The steps below will get you up and running with a local development environment. All of these commands assume you are in the root of this repository.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/); if you don’t have it yet, follow the installation instructions;
- [Docker Compose](https://docs.docker.com/compose/install/); refer to the official documentation for the installation guide.
- [Pre-commit](https://pre-commit.com/#install); for clean code .

## Build the Stack

This can take a while, especially the first time you run this particular command on your development system:

```bash
make build
```

Generally, if you want to emulate production environment use production.yml instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!

Before doing any git commit, pre-commit should be installed on your local machine:

```bash
pre-commit install
```

Also pre-commits can be run by:

```bash
pre-commit run --all
```

Failing to do so will result with a bunch of CI and Linter errors that can be avoided with pre-commit.

## Run the Stack

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development:

```bash
make start
```

To run in a detached (background) mode, just:

```bash
make startd
```

### Execute Management Commands

As with any shell command that we wish to run in our container, this is done using the `docker-compose -f docker-compose-local.yml run --rm` command:

```bash
docker-compose -f docker-compose-local.yml run --rm django python manage.py createsuperuser
```

Here, django is the target service we are executing the commands against.

See the make file for predefined management commands.
