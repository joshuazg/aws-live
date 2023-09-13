from flask import Flask, render_template, request, url_for
from pymysql import connections
import os
import boto3

customhost = "internshipdatabase.cpkr5ofaey5p.us-east-1.rds.amazonaws.com"
customuser = "admin"
custompass = "admin123"
customdb = "internshipDB"
custombucket = "joshua-internship"
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
    return render_template('publishIntern.html')

@app.route("/addInternFormCom", methods=['POST'])
def AddInternFormCom():

    job_title = request.form['job_title']
    job_desc = request.form['job_description']
    job_salary = request.form['job_salary']
    job_location = request.form['job_location']
    workingDay = request.form['workingDay']
    workingHour = request.form['workingHour']
    accomodation = request.form['accomodation']

    print("%s %s %s %s %s %s %s", job_title, job_desc, job_salary, job_location,
          workingDay, workingHour,accomodation)

    #insert_sql = "INSERT INTO student VALUES (%s, %s)"
    #cursor = db_conn.cursor()

    #cursor.close()

    #print("all modification done...")
    #return render_template('AddStudOutput.html', name=stud_name)



@app.route("/searchstud", methods=['GET'])
def get_intern_com_details():
    try:
        # Corrected SQL statement with placeholder
        statement = "SELECT intern_id, company_name FROM Internship"
        cursor = db_conn.cursor()
        
        # Fetch the result
        result = cursor.fetchone()

        if result:
            intern_id, company_name = result
            return render_template('try.html', name=intern_id, company_name=company_name)
        else:
            return 0
        
    except Exception as e:
        return str(e)
        
    finally:
        cursor.close()


@app.route("/updatestud", methods=['POST'])
def UpStud():
    try:
        stud = request.form['update_id']
        name = request.form['update_name']

        # Corrected SQL statement with placeholder
        statement_get = "SELECT stud_name FROM student WHERE stud_id = %s"
        cursor = db_conn.cursor()
        cursor.execute(statement_get, (stud,))
        
        # Fetch the result
        result = cursor.fetchone()

        if result:

            stud_name = result[0]
            statement = "UPDATE student SET stud_name = %s WHERE stud_id = %s"
            cursor.execute(statement, (name, stud))
          
            return render_template('updateStudent.html', new=name, id=stud, old=stud_name)
        else:
            return render_template('updateError.html', id=stud)
        
    except Exception as e:
        return str(e)
        
    finally:
        cursor.close()


        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
