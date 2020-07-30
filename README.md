# Project Title
- Classic system of registration, login and logout
and
- api rest Framework
## Technologies 

- PostgreSQL 11
- Django 3.0
- rest framework
- HTML/CSS


## Installation

### Install PostgreSQL
#### - Crear Usuario Postgres
```

```
#### - Create Database

```

```

#### - Install  Python

```

```
#### - Install  pip
```
sudo apt install python3-pip
```
#### -  Install  Environment
```
sudo pip3 install virtualenv
```

### Steps to Start Project


####  1.- Clone Repository
```
git clone https://github.com/anapao07/user_authentication.git

cd user_authentication
```
#### 2.- Create and Activate Virtual Environment
```
virtualenv -p python3.8 userenv
source userenv/bin/activate
```

#### 3.- Install Requirements
```
pip install -r requirements.txt
```

#### 4.- Perform Migrations
```
python manage.py migrate
```
## Start Application
```
python manage.py runserver
```

### Api
```
http://0.0.0.0:8000/api/
```
### App
```
http://0.0.0.0:8000/