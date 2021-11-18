import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="postgres",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html', error='')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = ''
    if request.method == 'POST':
        if request.form.get("login"):
            error = ''
            username = request.form.get('username')
            password = request.form.get('password')
            if username == '' or password == '':
                if username == '':
                    error += 'Заполните поле username! '
                if password == '':
                    error += 'Заполните поле password! '
                return render_template('login.html', error=error)
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            try:
                return render_template('account.html', full_name=records[0][1])
            except IndexError:
                return render_template('login.html', error='Пользователь отсутствует!')
            except Exception:
                return render_template('login.html', error='Что-то пошло не так!')
        elif request.form.get("registration"):
            return redirect("/registration/", error='')

    return render_template('login.html', error=error)


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        error = ''
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        if name == '' or login == '' or password == '':
            if name == '':
                error += 'Заполните поле name! '
            if login == '':
                error += 'Заполните поле login! '
            if password == '':
                error += 'Заполните поле password! '
            return render_template('registration.html', error=error)

        cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()

        return redirect('/login/', error='')

    return render_template('registration.html')
