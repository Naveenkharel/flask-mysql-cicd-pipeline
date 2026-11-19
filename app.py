import os
from flask import Flask
import pymysql
import time


app=Flask(__name__)

db_host = os.environ.get('DB_HOST', 'localhost')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')         
db_name = os.environ.get('DB_NAME', 'mydatabase')

def get_db_connection():
    retries=5
    while retries>0:
        try:
            connection=pymysql.connect(host=db_host,user=db_user,password=db_password,database=db_name)
            return connection
        except pymysql.MySQLError as e:
            retries -= 1
            time.sleep(2)
        return None

@app.route('/')
def hello():
    connection=get_db_connection()
    if connection:
        connection.close()
        return "<h1>Hello, successful connected to mysql!</h1>"
    else:
        return "<h1>Failed to connect to mysql!</h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)

