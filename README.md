gallery
=======

simple django application for uploading images and adding comments


setup
=======

requires python >= 2.6 && python-dev:

    apt-get install python-dev


create a virtualenv && activate it:

    virtualenv --no-site-packages project; cd project; source bin/activate


install django into a virtualenv:

    pip install django==1.4.3;


to show available versions:

    pip install yolk; yolk -V django


create a db if none exists:
    python manage.py syncdb


run the server!:

    python manage.py runserver
