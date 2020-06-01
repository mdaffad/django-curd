# Django-gitlab

Mirrored from : <a href=https://gitlab.com/mdaffad/django-gitlab>gitlab.com/mdaffad/django-gitlab</a>

## Django project with gitlab-ci

Django project using MySQL database engine and gitlab-ci configuration and mirrored to github remote repository

## How to Use

### 1. Build the virtual environtment and manage dependencies

Get directory on root project and run this in terminal

```bash
chmod +x build.sh
./build.sh
```

### 2. Start the virtual environtment

Get directory on root project and run this in terminal

```bash
source venv/Scripts/activate
```

### 3. Migrate and running django server

Before migrating make sure you have following database configuration in mysite/mysite/settings.py
Please follow this link <a href=https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-notes> https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-notes </a>

Get directory on root project and run this in terminal

```bash
python3 mysite/manage.py migrate
python3 mysite/manage.py runserver
```
