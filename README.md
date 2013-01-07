Gallery
=======

Simple django application for uploading images and adding comments.


## Quick Guide

Use `virtualenv` for a clean environment:

    virtualenv --no-site-packages project; cd project; source bin/activate


Install `django` & `pil` into the `virtualenv`:

    pip install django==1.4.3 pil


Show available versions of `django`:

    pip install yolk; yolk -V django


Clone the repository locally:

    git clone https://github.com/johndoevodka/gallery; cd gallery


Create a db if none exists:

    python manage.py syncdb


Run the server:

    python manage.py runserver


## Requirements
  *  `python` (>= 2.6)
  *  `python-dev` 
  *  `virtualenv` 
  *  `python-pip` 
  *  `django` (1.4)
  *  `pil`
