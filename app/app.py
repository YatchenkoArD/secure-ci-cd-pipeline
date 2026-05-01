from flask import Flask
import os

app = Flask(__name__)

# --- СЕКРЕТЫ ДЛЯ ТЕСТИРОВАНИЯ SECRET DETECTION ---
AWS_ACCESS_KEY_ID = "AKIAV7E5B6C7D8E9F0G1" 
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_URL = "postgresql://admin:SuperSecretPassword123@db-prod.finenomore.internal:5432/orders"
# ------------------------------------------------

@app.route('/')
def index():
    return "<h1>FineNoMore API is running</h1><p>Security scan in progress...</p>"

if __name__ == '__main__':
    # Включаем debug для разработки
    app.run(host='0.0.0.0', port=5000)