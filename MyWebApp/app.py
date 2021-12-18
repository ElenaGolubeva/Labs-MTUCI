import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
# Подключение к бд
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="8962240",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                return render_template('login.html', username=username, password=password, first_time=False,
                                       dateerror=False)

            try:
                cursor.execute("SELECT * FROM service1.users WHERE login=%s AND password=%s", (str(username), str(password)))
                records = list(cursor.fetchall())
                return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
            except IndexError:
                return render_template('login.html', username=username, password=password, first_time=False,
                                       dateerror=True)
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html', username="", password="", first_time=True, dateerror=False)


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')

        if not name or not login or not password:
            return render_template('registration.html', name=name, login=login, password=password, first_time=False, Len=True)
        if len(password)<=3:
            return render_template('registration.html', name="", login="", password="", first_time=True, Len=False)

        cursor.execute('INSERT INTO service1.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()
        return redirect('/login/')
    return render_template('registration.html', name="", login="", password="", first_time=True, Len=True)

