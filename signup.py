import MySQLdb
from flask import Flask as flask
from flask import redirect, url_for, request, render_template
import MySQLdb
app = flask(__name__, template_folder = 'template')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    connection = MySQLdb.connect('localhost', 'root', '25091813', 'Project')
    con = connection.cursor()
    if request.method == 'POST':
        name = request.form.['username']
        password = request.form.['password']
        email = request.form.['email']
        email_sql = "SELECT * from users WHERE email = " + "'" + email + "'"
        email_sql = f"SELECT * from users WHERE email = '{email}'"
        con.execute(email_sql)
        row = con.fetchone()
        if row is not None:
            error = 'r3c'
            render_template('index.html', error = error)

        username_sql = "SELECT * FROM users WHERE name = "  + "'"+ name + "'"
        con.execute(username_sql)
        row1 = con.fetchone()
        if row1 is not None:
            error = 'r3c'
            render_template('index.html', error = error)

        if row1 is None and row is None:
            stmt = "INSERT INTO users (name, email, password) VALUES (" + "'" + name + "'" + ", " + "'" +  email + "'" + ", " + "'" +   password+ "'" + ")"
            print(stmt)
            con.execute(stmt)
            connection.commit()
            con.execute("SELECT * FROM users")
            cols = con.fetchall()
            print(cols)

    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)
