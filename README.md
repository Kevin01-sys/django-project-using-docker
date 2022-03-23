# Django base

basic [Django](https://www.djangoproject.com/) project image to easy and quickly run up, using [Docker](https://www.docker.com/), [PostgreSQL](https://www.postgresql.org/), [Bootstrap 4](https://v4-alpha.getbootstrap.com/) and [JQuery](https://jquery.com/).

## Run the project

To run the project in a local enviroment, follow next steps:

1. **Install Docker**.

Download Docker from the [offical website](https://docs.docker.com/engine/installation/) and install it.

2. **Clone the project**.

Clone the project code locally using [Git](https://git-scm.com/):

    git clone git@github.com:augustakingfoundation/django_base.git

3. **Build the Docker image**

Make sure that Docker is running. Move to the root project folder and run the following command:

    docker-compose build

4. **Run the project**

Run the following command to run the project:

    docker-compose up

Now you can navigate to *localhost:8000* in your browser and you will see a Django project runing.

## Architecture

Python 3.6.0

Django 2.0

PostgreSQL 10.1

Bootstrap 4

Jquery 3.2.1


## keep in mind

1. If you will to create your own git repository, move to project root and remove the *.git/* folder configuration running the following comand:

    rm -rf .git/

2. It's amazing if you want to contribute. Please create your pull requests from your own branch to *development* branch.

3. Change the name of the root folder from *django_base* to your project name, and go to *docker-compose.yml* and edit image names from *djangobase* to your project name.

4. If you have any suggestion or you want to contribute, I want to recommend you register it on [utopian.io](https://utopian.io/).

***

**How was this repository built?**

- [Step by step guide to create a django_base project repository](https://steemit.com/utopian-io/@coffeesource.net/step-by-step-guide-to-create-a-djangobase-project-repository)
- [Pasos para crear el repositorio django_base](https://steemit.com/utopian-io/@kit.andres/pasos-para-crear-el-repositorio-del-proyecto-djangobase)

**How setup a new Django project?**


- [Cómo iniciar mi proyecto Django](https://steemit.com/utopian-io/@kit.andres/configuracion-inicial-de-mi-propio-proyecto-django-usando-el-repositorio-djangobase).
