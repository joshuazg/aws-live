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
def index():
    return render_template('search.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    # Execute a SQL query to search for the data
    cursor = db_conn.cursor()
    cursor.execute("SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, c.industry_involve 
    FROM Internship i INNER JOIN Company c WHERE i.com_id = c.com_id AND com_name LIKE %s", ('%' + query + '%',))
    results = cursor.fetchall()
    cursor.close()

    search_statement = """"""
    cursor = db_conn.cursor()
    cursor.execute(search_statement)
    search = cursor.fetchall()
    cursor.close()

    return render_template('search_results.html', results=results, search=search)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
