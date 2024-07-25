from flask import Flask, render_template
import mysql.connector
import datetime

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='mysql',
        database='logs_db',
        user='user',
        password='password'
    )
    return conn

@app.route('/')
def main():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS access_logs (id INT AUTO_INCREMENT PRIMARY KEY, access_time DATETIME)')
    cursor.execute('INSERT INTO access_logs (access_time) VALUES (%s)', (datetime.datetime.now(),))
    conn.commit()

    cursor.execute('SELECT * FROM access_logs')
    logs = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', logs=logs)

app.run(host='0.0.0.0', port=5000)
