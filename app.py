import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 🎯 ЦЕЛЬ 1: Secret Detection (Поиск секретов)
# Уязвимость: Жестко закодированный токен. Сканер (например, Gitleaks) найдет этот AWS ключ.
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE" 

def init_db():
    conn = sqlite3.connect('test.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)')
    conn.execute('INSERT OR IGNORE INTO users (id, username) VALUES (1, "admin")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # 🎯 ЦЕЛЬ 2: SAST и DAST (Cross-Site Scripting - XSS)
    # Уязвимость: Ввод пользователя (name) выводится на страницу без фильтрации.
    # DAST сканер (OWASP ZAP) сможет выполнить здесь вредоносный JavaScript код.
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

@app.route('/user')
def get_user():
    # 🎯 ЦЕЛЬ 3: SAST и DAST (SQL Injection)
    # Уязвимость: Прямая подстановка переменной в SQL-запрос вместо использования параметров.
    # SAST сканер (Semgrep/Bandit) укажет на строку с f-string как на критическую угрозу.
    user_id = request.args.get('id', '1')
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = f"SELECT username FROM users WHERE id = {user_id}"
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return f"User: {result[0] if result else 'Not found'}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    init_db()
    # 🎯 ЦЕЛЬ 4: SAST (Misconfiguration)
    # Уязвимость: Оставленный Debug-режим позволяет злоумышленнику видеть ошибки и выполнять код.
    app.run(host='0.0.0.0', port=5000, debug=True)