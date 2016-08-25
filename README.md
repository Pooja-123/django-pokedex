# Django Pokedex

This is a django-based Pokedex API.

## Setup

**Requirements**

 - python 2.6 +
 - [pip](https://pip.pypa.io/en/stable/installing/)
 - [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)
 - postgres

**Instructions**

. Clone repo

    git clone git@github.com:InclusionOrg/django-pokedex.git
    cd django-pokedex

. Make virtual enviroment

    mkvirtualenv django-pokedex

. Install dependencies

    pip install -r requirements.txt

. Create Database `project_001`

. Run migrations

    ./manage.py migrate

. Run Server

    ./manage.py runserver

The project will be up at `localhost:8000`

## Pokedex

![pokedex_schema]('./pokedex/schema.png')
