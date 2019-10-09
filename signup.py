from flask import Flask as flask
from flask import redirect, url_for, render_template, flash, session, request
import psycopg2 as psql
import MySQLdb
from login import login_api


#connection = psql.connect(user = "arnav.679.2022",
#                                  password = "25091813",
#                                  host = "127.0.0.1",
#                                  port = "5432",
#                                  database = "webapp")

connection = MySQLdb.connect("localhost", "root", "", "webapp")
con = connection.cursor()
app = flask(__name__, template_folder = 'templates')
app.secret_key = "A34562EF"
app.register_blueprint(login_api)
#con.execute('use webapp')
if __name__  == "__main__":
    app.run()
@app.route('/signup', methods = ['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        check_sql_1 = "SELECT * FROM users WHERE username = '{}'".format(username,)
        con.execute(check_sql_1)
        row = con.fetchone()
        if row != None:
            error = 'Username is already taken'
            return render_template('signup.html', error = error)
        else:
            email = request.form.get('email')
            check_sql_2 = "SELECT * FROM users WHERE email = '{}'".format(email)
            con.execute(check_sql_2)
            row = con.fetchone()
            if row != None:
                error = 'Email is already taken'
                return render_template('signup.html', error = error)
            else:
                insert_sql  = "INSERT into users (username, email, password) VALUES ('{}', '{}', '{}')".format(username, email, password)
                con.execute(insert_sql)
                connection.commit()
                if 'username' in session:
                    username = session['username']
                return redirect(url_for('login_api.login'))
                #redirect(url_for('login'))
    return render_template('signup.html')
