import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials (Security issue)
DB_USER = "admin"
DB_PASS = "password123"

# Database connection
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

# Creating a vulnerable users table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login successful!"
    else:
        return "Invalid credentials", 401

@app.route("/exec", methods=["POST"])
def exec_command():
    cmd = request.form.get("cmd")
    # OS Command Injection vulnerability
    output = os.popen(cmd).read()
    return output

if __name__ == "__main__":
    app.run(debug=True)
