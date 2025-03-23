# Secure Python Web App Example
from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Secure: Ensure database file permissions are restricted
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Secure: Hash passwords instead of storing plain text
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Secure: Use parameterized queries to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, hashed_password))
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        return "Login successful!"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=False)  # Secure: Disable debug mode in production
