## What's this?
Very simple and basic link shortening service built with Django.

## Running
cd into the project directory and input these commands in bash:
```
$ mkdir venv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ fission/manage.py makemigrations shortener
$ fission/manage.py migrate
$ fission/manage.py runserver
```

## Assumptions
- create_fake_users will be used to generate a non-zero number of fake users before any link shortening takes place
