from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
	query = 'SELECT name, age, MONTHNAME(created_at), DAY(created_at), YEAR(created_at) FROM friends'
	friends = mysql.query_db(query)
	print friends
	return render_template('index.html', friends=friends)

@app.route('/process', methods=['POST'])
def process():
	query = "INSERT INTO friends(name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
	data = {
		'name': request.form['name'],
		'age': request.form['age'],
	}
	mysql.query_db(query, data)
	return redirect('/')



app.run(debug=True)
