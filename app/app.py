from flask import Flask
import os

app = Flask(__name__)

# --- СЕКРЕТЫ ДЛЯ ТЕСТИРОВАНИЯ SECRET DETECTION ---
AWS_KEY = "AKIAIMNO789ABCDEF001" 
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GOOGLE_KEY = "AIzaSyA1234567890BCDEF1234567890ABCDEF"
CRITICAL_TOKEN = "api_key_1234567890abcdef1234567890abcdef"
DATABASE_URL = "postgresql://admin:SuperSecretPassword123@db-prod.finenomore.internal:5432/orders"
# ------------------------------------------------

@app.route('/')
def index():
    return "<h1>FineNoMore API is running</h1><p>Security scan in progress...</p>"

if __name__ == '__main__':
    # Включаем debug для разработки
    app.run(host='0.0.0.0', port=5000)