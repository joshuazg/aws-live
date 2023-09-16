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

@app.route("/", methods=['GET'])
def display_internship():

    #Get All Internship
    statement = "SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, i.accommodation, i.job_description, FROM Internship i, Company c"
    cursor = db_conn.cursor()
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.close()

    return render_template('index.html', internship = result)    

@app.route('/index/job_details/<int:id>')
def jobDetails(id):

    #Get Internship details
    details_statement = "SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, i.accommodation, i.job_description, c.product_service, c.industry_involve, c.person_incharge, c.contact_no, c.email FROM Internship i, Company c WHERE intern_id = %s"
    cursor = db_conn.cursor()
    cursor.execute(details_statement, (id))
    details = cursor.fetchone()
    cursor.close()
    
    return render_template('job_details.html', internship = details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
