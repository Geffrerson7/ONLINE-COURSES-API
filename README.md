# ONLINE-COURSES-API

## Description
It is an API for purchasing online courses.

## ERD


## Local Installation

Clone the repository.

```bash
$ https://github.com/Geffrerson7/ONLINE-COURSES-API.git
```

Go to the project directory.

```bash
$ cd ONLINE-COURSES-API
```

Create a virtual environment.

```sh
$ virtualenv venv
```
Activate the virtual environment.
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Install the dependencies.

```sh
(env)$ pip install -r requirements.txt
```
Run the migrations.
```sh
(env) $ python manage.py makemigrations
```
```sh
(env) $ python manage.py migrate
```

Run the project
```sh
(env)$ python manage.py runserver
```

And navigate to the route
```sh
http://127.0.0.1:8000/
```

## Project installation in Docker

Clone the repository

```bash
$ git clone https://github.com/Geffrerson7/ONLINE-COURSES-API.git
```

Go to the project directory.

```bash
$ cd ONLINE-COURSES-API
```

Run the command
```sh
$ docker-compose up
```

And navigate to the route
```sh
http://127.0.0.1:8000/
```

## Technologies y programming languages 

* **Python** (v. 3.11.2) [Source](https://www.python.org/)
* **Django** (v. 4.2.1)  [Source](https://www.djangoproject.com/)
* **Django Rest Framework** (v. 3.14.0) [Source](https://www.django-rest-framework.org/)
* **django-cors-headers** (v. 4.0.0) [Source](https://pypi.org/project/django-cors-headers/)
* **Simple JWT** (v. 5.2.2) [Source](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* **drf-yasg** (v. 1.21.5) [Source](https://drf-yasg.readthedocs.io/en/stable/)
* **mercadopago** (v. 2.2.0) [Source](https://github.com/mercadopago/sdk-python)


## Author
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)