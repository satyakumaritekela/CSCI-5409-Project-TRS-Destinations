import os
import mysql.connector
import requests
from flask import Flask, jsonify, request
from flask_material import Material

sql_db = mysql.connector.connect(
  host="tourism-database.ckl1wer2rqyx.us-east-1.rds.amazonaws.com",
  user="root",
  passwd="password",
  database="TRS",
  port="3306"
)

cursor = sql_db.cursor()

app = Flask(__name__)
app.secret_key = os.urandom(24)
Material(app)

@app.route('/destinations', methods=['GET', 'POST'])
def destinations():
    keyword = request.args.get('keyword', '')
    print (keyword)
    query = 'SELECT * from booking_destinations where name LIKE %s'
    try:
        cursor.execute(query, ("%" + keyword + "%",))
        result_sql = cursor.fetchall()
        return jsonify(result_sql)
    except Exception as e:
        # print (str(e))
        return jsonify([])


@app.route('/destination_by_id', methods=['GET', 'POST'])
def destination_by_id():
    idn = request.args.get('id')
    query = 'SELECT * from booking_destinations where id = ' + str(idn)
    try:
        cursor.execute(query)
        result_sql = cursor.fetchall()
        return jsonify(result_sql)
    except Exception as e:
        print (str(e))
        return jsonify("Some Exception Occured")
