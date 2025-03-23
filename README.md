# Secure Code Review Task

## Task Overview
In this task, I reviewed a Python web application to identify security vulnerabilities and recommend improvements. The code was reviewed for common issues like 
**SQL Injection**, **password security**, and **debug mode** exposure.

## Vulnerable Code
The original code contained several vulnerabilities:
1. SQL Injection: The user input was directly embedded into the SQL query, allowing attackers to manipulate the query.
2. Plain Text Passwords: The application stored passwords in plain text, which is insecure.
3. Debug Mode: The Flask application ran in debug mode, exposing sensitive information about the system.

## Secure Code
I applied the following security best practices to secure the application:
1. Parameterized Queries: I replaced the vulnerable SQL query with a parameterized query to prevent SQL injection attacks.
2. Password Hashing: Instead of storing plain text passwords, I used SHA-256 hashing to securely store and compare passwords.
3. Disabling Debug Mode: I turned off Flask's debug mode to avoid exposing sensitive information about the application in a production environment.

## Files
1. `vulnerable_code.py`: The original code with security flaws.
2. `secure_code_review.py`: The improved code with security fixes.
3. `README.md`: This file, explaining the task and code changes.
