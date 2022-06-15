

<div style="text-align:center; width: 50%; margin-left: 25%; margin-right: 50%"><img src="img/taskello_sign.png" /></div>

# Introduction
Useful and simple task planner written in Python<br />
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

# VM with running application
## About

### Taskello - Linux Ubutu 22.04 LTS server:
* the virtual machine includes:
  * MySQL Server
  * Taskello configured project:
      - github: https://github.com/pangeon/Taskello


The machine configuration includes port forwarding, which allows access to:
- Putty SSH
- Browser

**Taskello.vbox-prev** configuration file:
```
<Network>
  <Adapter slot = "0" enabled = "true" MACAddress = "080027C2BF57" type = "82540EM">
    <NAT>
      <Forwarding name = "Rule 1" proto = "1" hostport = "909" guestport = "22" />
      <Forwarding name = "Rule 2" proto = "1" hostport = "80" guestport = "5000" />
    </NAT>
  </Adapter>
</Network>
```

## Prepare environment for work:
1. Install on your PC machine: [Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)

2. Download from Google Drive prepared [VM - Ubuntu Server 22.04 LTS](https://drive.google.com/drive/folders/1_I8ncht73KGMFiQPxfCGAd6vTOVJUFb8?usp=sharing) with ready-made appplication.

## Running:

1. After starting the machine, enter:
      - login: **taskello**
      - password: **root**
2. Go to the Taskello folder
3. Enter the command:
    ``` 
    source venv/bin/activate
    ```
4. Run the applications:
    ```
    flask run -h 0.0.0.0 -p 5000
    ```
5. Open a browser on localhost

Access to the database is possible after issuing the command:

```
mysql -u dian_user -p
$ password: dian_pass_2021MAY
```


# Changelog

- 1.0.0 - full data edition via page without edit task assignments
- 1.1.0 - secured password, added hash function SHA-256
- 1.2.0 - validation data input form, fixed function SHA-256
- 1.2.1 - fixed problems with db create scripts
- 1.3.0 - added polish language support

# Other languages support

- Change language symbol in [routes.py](./app/routes.py) variable lang **["PL", "ENG"]**
- Support polish and english

# Problems and solutions:

- [PowerShell says “execution of scripts is disabled on this system.”](./hints/venv-windows-problem.md)

# Online documentation

## Flask

- [Official documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Mega Flask Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask with raw SQL](https://codeshack.io/login-system-python-flask-mysql/)


# Contact and support

- Kamil Cecherz - kamil.cecherz@gmail.com
