from flask import Flask, render_template, request, url_for
from pymysql import connections
import os
import boto3

customhost = "database-1.czj7uvclfwmy.us-east-1.rds.amazonaws.com"
customuser = "admin"
custompass = "admin123"
customdb = "internshipDB"
custombucket = "bucket-internship1"
customregion = "us-east-1"


app = Flask(__name__, static_folder='assets')

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}


def get_internships():
    try:
        # Corrected SQL statement with placeholder
        statement = "SELECT * FROM Internship"
        cursor = db_conn.cursor()
        
        # Fetch the result
        cursor.execute(statement)
        internships = cursor.fetchall()

        return internships
    except Exception as e:
        return str(e)
        
    finally:
        cursor.close()
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
