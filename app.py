from flask import Flask, render_template, request, url_for
from pymysql import connections
import os
import boto3

customhost = "internshipdatabase.cpkr5ofaey5p.us-east-1.rds.amazonaws.com"
customuser = "admin"
custompass = "admin123"
customdb = "database-1"
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


@app.route("/displayIntern", methods=['GET'])
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
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)