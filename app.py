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
table = "Internship"

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('try.html')
    
@app.route("/", methods=['GET'])
def get_intern_com_details():
    try:
        # Establish a database connection
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor(dictionary=True)  # Use dictionary cursor for easier data manipulation
        
        # Corrected SQL statement to select all rows
        statement = "SELECT intern_id, company_name FROM Internship WHERE intern_id = 1"
        
        # Fetch all rows
        cursor.execute(statement)
        results = cursor.fetchall()

        if results:
            # Pass the results to the HTML template
            return render_template('try.html', results=results)
        else:
            return "No data found."

    except Exception as e:
        return str(e)

    finally:
        cursor.close()
        db_conn.close()
              
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
