# Assessment: Data Representation Project

by Sarah McNelis

<br>

## Introduction

This repository contains my project work for Data Representation as part of my Higher Diploma in Computing in Data Analytics. 

<br>
 
## Setup

### Install the following

1. Download and install [anaconda](https://docs.anaconda.com/anaconda/install/index.html).
2. Download and install [cmder](https://cmder.app/).
3. Download and install [notepad++](https://notepad-plus-plus.org/downloads/)
4. Download and install [wampserver](https://www.wampserver.com/en/)

### Requirements text file

`requirements.txt` contains a list of all the python packages requried to import in order to run the progam. 

### Running a python file

1. Open the command line at the appropriate respository. 
2. Type `python ` followed by the filename you wish to execute. 
3. The file will run. 

### Running a html file

1. Open the desired file in Notepad++
2. Click View on the toolbar
3. And click View Current File in and choose your preferred browser. 

### Accessing database table

1. Open wampserver
2. Click on MySQL
3. And click on MySQL console
4. Once the console is open type `SHOW DATABASES;`
5. Now type `USE arrivals_at_snn`
6. Once you are in the database type `SHOW TABLES;`. This shows all tables available within that database. 
7. To see the arrivals table type `SELECT * FROM arrivals;`. This will produce an arrivals table. This table will be accessed and updated using SQL commands in my python scripts. See `arrivalsDAO.py` and `link_to_db.py`.

### Hosting the server

I have chosen to host my server on ... 
You can find the host server link [here]() 

<br>

## What to expect
This repository contains:

- `arrivals.html` - where I created a webpage based on Shannon Airport arrival information. In this document you will find CRUD operations in the script section which allow the webpage to consume the API. 

- `rest_server.py` - which creates an application server that will implement a RESTful API using Flask. 

- `arrivalsDAO.py` - this program creates a class for arrivals which contains functions to implement SQL commands in a python script. This is imported into the next file to link to the database. 

- `link_to_db.py` - this is where all the SQL commands in the previous file are executed on the database.

This repository also contains ... 

<br>


## Credits

- For this project I heavely relied on my lecturer's notes. You can access his github repository [here](https://github.com/andrewbeattycourseware/datarepresentation).


<br>

## References

- https://docs.python-guide.org/dev/virtualenvs/
- https://flask.palletsprojects.com/en/latest/
- https://realpython.com/python-requests/
- https://requests.readthedocs.io/en/latest/
- https://docs.python.org/3/library/urllib.html
- https://realpython.com/flask-connexion-rest-api/
- https://getbootstrap.com/docs/3.4/css/ 
- https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
- 

<br>

## End