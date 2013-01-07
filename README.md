gallery
=======

simple django application for uploading images and adding comments


setup
=======

apt-get install python-dev

virtualenv --no-site-packages project; cd project; source bin/activate; (activate virtualenv)

pip install yolk; yolk -V django (show available versions of package); pip install django==1.4.3;



python manage.py syncdb; (create a database if there is none)

python manage.py runserver; (run the server!)
