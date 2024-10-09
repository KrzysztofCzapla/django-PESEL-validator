# django PESEL validator

# Configuration & Installation

## 1) Add .env to config folder
### example: 
#### `SECRET_KEY=django-insecure-r^bvaqb2m(n7w)!1_v@3_#6tej2mtx=z3ad2-q8$+$-nh!1hf#`


#### `DEBUG=1`

## 2) Install dependencies
### You can install dependencies using either docker with poetry or simply download the libraries and runserver manually.

### Docker way
#### 1) install docker with docker compose
#### 2) ```docker-compose up```

### Manual way
#### 1) `pip install -r requirements.txt`
#### 2) python manage.py runserver 0.0.0.0:8000

# Usage

### Just go to localhost:8000 and check a PESEL ;)