
# Polish Case Trainer Web API

This fork of the [original CLI version](https://github.com/tombusby/PolishCaseTrainer) of the adds a REST http interface to the question generation logic. 

## Installation

Clone the repository.

```
git clone https://github.com/davidhelbig/casetrainer-api.git

cd casetrainer-api
```

The project manages dependencies using [pipenv](https://pipenv.pypa.io/en/latest/). Make sure pipenv is available and install the dependencies:

```
pipenv install

# if you want to run tests
pip install --dev
```

The project uses [hug](https://github.com/hugapi/hug) to expose an http API. From within your virtual environment (if you used pipenv, spawn it with `pipenv shell`), run

```
hug -f api.py
```
A local development server will start (by default on port 8000) and you can start requests to the API.

## API Documentation

By default, `hug` will auto-generate an API documentation and return it when queried for an endpoint that is not defined.
So if you request the root URL of the API with curl or httpie, you will see a short documentation of the current endpoints:

```
curl localhost:8000
```

## Deployment

The repository comes with a Procfile for deployment on heroku.
For manual deployment with a wsgi server like uwsgi or gunicorn, use the auto-generated module `api:__hug_wsgi__`.
