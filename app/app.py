import subprocess
from flask import Flask, request
import os

app = Flask(__name__)

AWS_KEY = "AKIAIMNO789ABCDEF001" 
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GOOGLE_KEY = "AIzaSyA1234567890BCDEF1234567890ABCDEF"
CRITICAL_TOKEN = "api_key_1234567890abcdef1234567890abcdef"
DATABASE_URL = "postgresql://admin:SuperSecretPassword123@db-prod.finenomore.internal:5432/orders"
# ------------------------------------------------

@app.route('/')
def index():
    return "<h1>FineNoMore API is running</h1><p>Security scan in progress...</p>"

@app.route('/dns')
def dns_lookup():
    hostname = request.args.get('hostname')
    cmd = "nslookup " + hostname
    data = subprocess.check_output(cmd, shell=True)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)