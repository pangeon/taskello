

<div style="text-align:center; width: 50%; margin-left: 25%; margin-right: 50%"><img src="img/taskello_sign.png" /></div>

# Introduction
Useful and simple CRM written in Python<br />
<!-- See working appplication on page: [here]() -->

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
3. Debug interactive session:
  ```
  python app.py
  ```
# Changelog

- 1.0.0 - full data edition via page without edit task assignments
- 1.1.0 - secured password, added hash function SHA-256
- 1.2.0 - validation data input form, fixed function SHA-256
- 1.2.1 - fixed problems with db create scripts

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

- Kamil Cecherz - kamil.cecherz@gmail.com
