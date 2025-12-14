# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'Exin@1234'  # Replace with a strong secret key

# MySQL connection config
db_config = {
    'user': 'exin',
    'password': 'Exin@1234',
    'host': '192.168.0.102',
    'database': 'garudabase'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return render_template('register.html', error='Please fill out all fields.')

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM users WHERE username=%s', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return render_template('register.html', error='Username already taken.')

        hashed_password = generate_password_hash(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username=%s', (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect('/additional_info')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/additional_info', methods=['GET', 'POST'])
def additional_info():
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        address = request.form['address']
        phone = request.form['phone']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET address=%s, phone=%s WHERE id=%s',
                       (address, phone, session['user_id']))
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('additional_info.html', message='Information updated successfully!')
    return render_template('additional_info.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5051)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=True)


