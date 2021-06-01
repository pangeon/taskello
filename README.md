# Dianetello

Dianet company CRM.<br />
See working appplication on page: [here](http://192.168.0.69:5000/)

# Deployment guide

## 1) Requirements

- **Windows**, download and install:

  - [Python 3](https://www.python.org/downloads/)
  - [MySQL Server](https://dev.mysql.com/downloads/mysql/)

- **Linux**, run command in bash shell:
  ```
  sudo apt update
  sudo apt -y upgrade
  sudo apt install -y python3-pip
  sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
  sudo apt install -y python3-venv
  ```

## 2) Virtual environment

- Create in master dir:

  ```
  python -m venv venv
  ```

- Start:

  - Linux

  ```
  source venv/bin/activate
  ```

  - Windows

  ```
  venv\Scripts\activate
  ```

- Stop:

  ```
  deactivate
  ```

## 3) Install dependencies

- When you're running virtual env download files with pip:

  ```
  pip install mysql-connector-python
  pip install Flask
  pip install flask-wtf
  pip install email-validator
  ```

## Model

- More details abount database schema on: [data/model/schema.txt](./data/model/schema.txt) and [data/sql/create_tables.sql](./data/sql/create_tables.sql)

  ![](img/schema.PNG)

## Connecting to database

- You can use db_manager on [utils](./utils/db_manager/mysql_connector.py)

## Create data model and fill the table with sample data

1. Using **MySQL** and create database dian_db, use file [create_database.sql](./data/sql/create_database.sql)

2. Start mysql service and run **init.py**

   - If you want create new database, set **create** variable to **YES**.<br />
   - If you want delete database, set **create** variable to **NO**.

- Windows

  ```
  venv\Scripts\activate
  python init.py
  ```

- Linux

  ```
  source venv/bin/activate
  python init.py
  ```

## Run

1. Activate virtual environment in your machine:
2. Run HTTP server with Flask:

   ```
   flask run  -h <host>  -p <port>
   ```

- example:

  ```
  flask run
  flask run -h 0.0.0.0 -p 5000
  ```

# Changelog

- 0.0.1 - root of application
- 0.0.2 - added simple project structure
- 0.0.3 - created database model to project
- 0.0.4 - added virtual env
- 0.0.5 - created connector util for MySQL
- 0.0.6 - preparing sample data to insert
- 0.0.7 - selected data using app interface
- 0.0.8 - inserted data using app interface
- 0.1.8 - created controllers for app
- 0.1.9 - support for all CRUD operations
- 0.1.10 - created inititiation data files
- 0.2.10b - created sample command line user interface
- 0.3.0c - first sample web page with Flask
- 0.3.1c - created view for data from database
- 0.3.2c - first HTML view and data handle
- 0.4.0c - built web service - full view
- 0.4.1c - production version for vm ubuntu linux
- 0.5.0c - added posibility to add new task
- 0.5.1c - refactoring code for flask app
- 0.5.2c - refactoring flask templates
- 0.6.0c - added posibility to login existing user
- 0.7.0c - added posibility to registry new user
- 0.7.1c - fixed bugs with profile account and login
- 0.8.0c - added posibility profile data edit:
  - 0.8.1c - enabled name na surname edition
  - 0.8.2c - change password
  - 0.8.3c - function delete own profile
- 0.8.4c - fixed password form and validation data

# Preview

- 0.9.0c - possiblity assign tasks to profile
- 1.0.0c - full data edition via page
- 1.1.0c - secure password, hash function
- 2.1.0c - new look with bootstrap 4

# Problems and solutions:

## Windows:

- [PowerShell says “execution of scripts is disabled on this system.”](./hints/venv-windows-problem.md)

## Linux

# Online documentation

## Flask

- [Official documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Mega Flask Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask with raw SQL](https://codeshack.io/login-system-python-flask-mysql/)

## MySQL

# Contact and support

- Kamil Cecherz - kamil.c@dianet.pl
