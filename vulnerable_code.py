# Insecure Python Web App Example
from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Vulnerability: No input validation or secure connection
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Vulnerability: SQL Injection (User input directly in query)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return "Login successful!"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=True)  # Vulnerability: Debug mode exposes sensitive data

