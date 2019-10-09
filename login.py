from flask import Flask as flask
from flask import redirect, render_template, session, flash, url_for, request
import MySQLdb
import importlib
from flask import Blueprint

importlib.import_module('signup')

login_api = Blueprint('login_api', __name__)
#app = flask(__name__, template_folder = 'templates')
connection = MySQLdb.connect("localhost", "root", "", "webapp")
con = connection.cursor()
#app.secret_key = "A34562EF"
@login_api.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        check_sql = "SELECT password FROM users WHERE username = '{}'".format(username)
        con.execute(check_sql)
        row = con.fetchone()
        if row[0] == password:
            if 'username' in session:
                username = session['username']
            #return redirect(url_for('index'))
            return "Logged in as " + username
        else:
            error = 'Login credentials are wrong, Please try again.'
            return render_template('login.html', error = error)
    return render_template('login.html')
