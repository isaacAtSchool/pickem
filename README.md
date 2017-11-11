# Pick 'Em and Win 'Em
 It's not betting but it sure feels like it 

# Getting Started
**Instructions not completely test**
00. Download MySQL and set up a root user.
0. initalize the MySQL database and database user that the application will be using. For now I have the instructions from the tutorial that I'm basing this project off of. Updated instructions will come when I've working out the database code for Pick 'Em and Win 'Em. changing this code should be fairly easy.

```bash
mysql> CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE DATABASE dreamteam_db;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';
Query OK, 0 rows affected (0.00 sec)

```
1. Download the "Pickem" folder from the repo. Save the pickem folder in an empty location in your file system.
2. Download virtualenv. We are using python 2.7!

```bash
pip install virtualenv
```
3. create a virtual environment along side the pickem folder called pickem-virtualenv
```bash
virtualenv pickem-virtualenv
```
4. activate the virtual environment
```bash
source pickem-virtualenv/bin/activate
```
5. your prompt should now have **(pickem-virtualenv)** in front of it.
6. now download the dependencies
```bash 
pip install flask flask-sqlalchemy mysql-python flask-login flask-migrate
```
7. set up your environment variables
```bash
export FLASK_APP=run.py
export FLASK_CONFIG=development
```
8. map the models built in app/models.py then push these mappings to the database. Note that the database uri is in the instance/config.py module
```bash
flask db init
flask db migrate
flask db upgrade
```

9. Basic set up is done. Now start the flask mini server
```bash
flask run
```

10. You should see that the server is running on your localhost on port 5000. You should see something like
```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

11. Now visit http://127.0.0.1:5000/  in your browser of choice and see our home page. 


# Useful links
## Hosting/Server set-up
[Setting up a flask app in apache](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)

[Other server options under the "Self Hosted Options" section](http://flask.pocoo.org/docs/0.12/deploying/)
