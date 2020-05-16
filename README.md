# django-curd
CURD system with django-python framework

## 1. Start the virtual environtment and manage dependencies
In root project run
```
dependencies.bat
```

## 2. MySQL Engine (If found mysqlclient error)
Get directory on root project

If you have version problem, find the exact wheel file with your version on 
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

## 3. Setting up the mysql user
1. Create user in mysql with same user-information in settings.py
```
mysql> CREATE USER 'djangoadmin'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345';
```

2. Create database with same nama in settings.py and grant privileges
```
mysql> CREATE DATABASE djangodatabase;
mysql> GRANT ALL PRIVILEGES ON djangodatabase.* TO 'djangoadmin'@'localhost';
```

3. Migrate database. Go to the directory of manage.py
```
python manage.py migrate
```