# Risk Model Builder

## Overview

* Python 3.5.2

* pip 9.0.1

## Running Tests

### Dependencies

    sudo pip install django
    sudo pip install djangorestframework

    sudo pip install jsonfield

    (django-jsonfield)[https://github.com/dmkoch/django-jsonfield]


    sudo pip install django-nose
    sudo pip install lxml
    sudo pip install defusedxml

## Developer's Guide

For my all future reference, I'm going to document the entire process of creating a REST API in Python/Django.

### Creating an App

First you need to create a project, which is comprised of one or more apps:

    django-admin startproject risk_model_api


Then you can add an app to the project:

    python manage.py startapp risks

In our particular case, "risks" is a REST API app.


### Manage Database

#### Migrating

    python manage.py makemigrations
    python manage.py migrate

You will need to run this command everytime you create or modify a model (in the model-view-controller sense).

#### Cleaning Up

The following command will cleanup the database:

    python manage.py flush


#### Loading Data

The following command will 

    python manage.py loaddata fixtures/test_data.json

Where `test_data.json` is a fixture file with the test data.

### Runnning the App

    python manage.py runserver

This command will run the app, which can be browsed at (this address)[http://localhost:8000/].

### Invoking from the Shell

The standard way to start an interactive session:

    python manage.py shell

But a better way is installing (django-extensions)[https://github.com/django-extensions/django-extensions]:

    sudo pip install django-extensions

You will also need to add 'django-extensions' to `INSTALLED_APPS`.

`shell_plus` will reload the environment for the notebook every time any modifications are applied to the code.

And also iPython and Jupyter:

    sudo pip3 install ipython
    sudo pip3 install jupyter

This way you may run commands in an interactive iPython Jupyter notebook:

    python manage.py shell_plus --notebook

This will open a web browser window with the Jupyter project tree. Create a notebook by clicking `new > Django Shell-Plus` and type the code you wish to experiment with:

![An Interactive Jupyter iPython Django Shell-Plus Notebook](images/jupyter1.png)

Note `%load_ext autoreload` and `%autoreload 2`: These will reload any modifications in the project source files. 

### Test Coverage

To run test coverage you will to install django-nose:

    sudo pip install django-nose

And add it to your `settings.py`:

	INSTALLED_APPS = [
	    
	    ...
     
	    'django_nose',
	]
     
    ...
     
	TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
     
	NOSE_ARGS = [
	    '--with-coverage',
	    '--cover-package=foo,bar',
	]

## Sublime Text

Just for future reference, here are some nice plugins for sublime text 3:

* (Sublime Pretty JSON)[https://github.com/dzhibas/SublimePrettyJson]: For formatting JSON.