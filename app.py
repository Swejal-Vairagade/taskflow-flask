from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='taskflow_db'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    c = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        c.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s", (title, description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        c.execute("SELECT * FROM tasks WHERE id = %s", (id,))
        task = c.fetchone()
        conn.close()
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT
    app.run(host='0.0.0.0', port=port)

 
