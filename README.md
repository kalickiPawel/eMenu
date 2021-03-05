# eMenu REST API
Design and implementation of an independent Menu service, serving as an online restaurant menu card.

---

[![Build Status](https://travis-ci.com/kalickiPawel/eMenu.svg?branch=main)](https://travis-ci.com/kalickiPawel/eMenu)
[![codecov](https://codecov.io/gh/kalickiPawel/eMenu/branch/main/graph/badge.svg?token=9A449H5QHH)](https://codecov.io/gh/kalickiPawel/eMenu)
![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework)

## Features :sparkles:

### public

1. REST API for menu cards management.
2. Create multiple menu cards with unique names.
3. Each menu card can contain any number of dishes.
4. Dish model: name, description, created_at, updated_at, price, preparation_time, vegan.
5. Menu model: name, description, created_at, updated_at.
6. API must be secured to prevent unauthorized access

### private

1. REST API for viewing non-empty menu cards.
2. Ability to sort the list by name and number of dishes, using parameters GET
3. Filtering the list by name and period of addition and last update
4. Card detail showing all the card information and dishes in the card.

### mail reporting

1. Sending an email once a day at 10:00 to all application users
2. The email contain information about new added and recently modified recipes
3. Information is sending only about those recipes that have been modified in previous day.

## Getting started :hammer_and_wrench:

### Cloning the repository
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/kalickiPawel/eMenu
$ cd eMenu
```

### Working with `virtualenv`
If you are using `virtualenv`, make sure you are running a python3 environment. Installing via `pip3` in a v2 environment will not configure the environment to run installed modules from the command line.
To setup virtual environment follow:
- `python3 -m pip install -U virtualenv`
- `python3 -m virtualenv venv`
- `.venv\Scripts\activate` or `source .venv/bin/activate`

### Installing required packages


```shell
$ pip install -r requirements.txt
```

### Creating environment variables :lock:
To prevent the unauthorised access to our resources we need to secure sensitive data. .env file lets you customize your individual working environment variables. Below is the sample `.env` file.
My app use environment variables for correct work.

Please change this data before deploy production.

Only for `DEBUG`
```dotenv
DJANGO_DEBUG=1
APP_SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
APP_DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgress
POSTGRES_USER=postgress
POSTGRES_PASSWORD=postgress
DB_HOST=db
DB_PORT=5432
```

### Performing database migration
```shell
$ python manage.py migrate
```
### Creating `superuser`
To manage the REST API resources User account is needed.
Users could be created via admin panel but for use this panel
you need `SuperUser` permissions. To create `SuperUser` in Django
perform:

```shell
$ python manage.py createsuperuser --email admin@example.com --username admin
```
### Running server
```shell
$ python manage.py runserver
```
### Show the results
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
or [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) 
to view documentation.

## Alternative `docker-compose` solution :whale:

### Run the app
Run the docker-compose up command from the top level directory for project. 
(where the file is located). At first, you need to build docker-compose file next make database migrations.
```sh
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose -f docker-compose.yml exec django python manage.py migrate --noinput
```
### Show the results
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
or [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) 
to view documentation.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ py.test