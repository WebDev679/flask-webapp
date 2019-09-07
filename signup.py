import MySQLdb
from flask import Flask as flask
from flask import redirect, url_for, request, render_template
import login
import pymysql
app = flask(__name__, template_folder = 'template')


@app.route('/signup', methods = ['GET', 'POST'])
def siggitgit vnup():
    connection = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
    )
    con = connection.cursor()
    con.execute('use Project')
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        email1 = "SELECT * from users WHERE email = " + "'" + email + "'"
        con.execute(email1)
        row = con.fetchone()
        if row is not None:
            return 'Email already taken'
            return redirect(url_for('login'))
        username1 = "SELECT * FROM users WHERE name = "  + "'"+ name + "'"
        con.execute(username1)
        row1 = con.fetchone()
        if row1 is not None:
            return 'Username already taken'
            return redirect(url_for('signup'))

        stmt = "INSERT INTO users (name, email, password) VALUES (" + "'" + name + "'" + ", " + "'" +  email + "'" + ", " + "'" +   password+ "'" + ")"
        print(stmt)
        con.execute(stmt)
        con.execute("SELECT * FROM users")
        cols = con.fetchall()
        print(cols)
        f





    return render_template('sign_up.html')
    return redirect(url_for('/login'))
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)
