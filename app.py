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
    home_statement = """SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, c.industry_involve 
    FROM Internship i INNER JOIN Company c WHERE i.com_id = c.com_id"""
    cursor = db_conn.cursor()
    cursor.execute(home_statement)
    result = cursor.fetchall()
    cursor.close()

    #Get Industry involve
    indus_statement = "SELECT cate_name FROM Category"
    cursor = db_conn.cursor()
    cursor.execute(indus_statement)
    indus = cursor.fetchall()
    cursor.close()

    return render_template('index.html', internship = result, category = indus)    

@app.route('/index/job_details/<int:id>')
def jobDetails(id):

    #Get Internship details
    details_statement = """SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, i.accommodation, i.job_description, c.product_service, c.industry_involve, c.person_incharge, c.contact_no, c.email 
    FROM Internship i INNER JOIN Company c WHERE i.com_id = c.com_id AND intern_id = %s"""
    cursor = db_conn.cursor()
    cursor.execute(details_statement, (id))
    details = cursor.fetchone()
    cursor.close()
    
    return render_template('job_details.html', internship = details)

@app.route('/index/job_listing/<string:cate>')
def jobList(cate):

    #Get Specific Listing 
    cate_statement = """SELECT i.intern_id, c.com_name, i.job_title, i.intern_salary, i.location, i.workingDay, i.workingHour, c.industry_involve 
                        FROM Internship i INNER JOIN Company c WHERE i.com_id = c.com_id AND c.industry_involve = %s """
    cursor = db_conn.cursor()
    cursor.execute(cate_statement, (cate))
    list = cursor.fetchall()
    cursor.close()
    
    return render_template('job_listing.html', listing = list, type = cate)

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from Company ORDER BY com_id"
            cur.execute(query)
            com = cur.fetchall()
        else:    
            query = "SELECT * from Company WHERE com_name LIKE '%{}%' ORDER BY id DESC LIMIT 20".format(search_word,search_word,search_word)
            cur.execute(query)
            numrows = int(cur.rowcount)
            com = cur.fetchall()
            print(numrows)
    return jsonify({'htmlresponse': render_template('response.html', employee=com, numrows=numrows)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
