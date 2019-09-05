from flask import Flask as flask
from flask import redirect, url_for, render_template, request
import MySQLdb

app = flask(__name__, template_folder = 'template')
connection = MySQLdb.connect('localhost','root', '')
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    cursor = connection.cursor()
    if request.method == 'POST':
        name  = request.form('username')
        passw = request.form('password')
        email = request.form('email')

    return render_template('index.html')
