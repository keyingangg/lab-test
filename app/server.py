from flask import Flask, request, redirect, render_template, send_from_directory
import re
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

app = Flask(__name__, template_folder='.', static_folder='.')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)

# Load common password list into memory
with open("common-passwords.txt", "r") as f:
    common_passwords = set(p.strip() for p in f)

# OWASP C6-based validation
def is_password_valid(password):
    if password in common_passwords:
        return False
    if len(password) < 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    password = request.form.get("password", "")
    if not is_password_valid(password):
        return render_template("index.html")  # Stay on homepage if invalid
    return render_template("welcome.html", password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
