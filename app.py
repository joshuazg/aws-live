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

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/index", methods=['GET'])
def view_internship(internship_id):

    statement = "SELECT * FROM Internship WHERE intern_id = %s"
    cursor = db_conn.cursor()
    cursor.execute(statement, (internship_id))
    result = cursor.fetchone()
    cursor.close()

    com_statement = "SELECT * FROM Company WHERE com_id = %s"
    com_cursor = db_conn.cursor()
    com_cursor.execute(com_statement, (result[1]))
    com_result = com_cursor.fetchone()
    com_cursor.close()

    return render_template('index.html', intern=result, com=com_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
