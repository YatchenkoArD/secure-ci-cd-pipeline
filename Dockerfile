# 🎯 ЦЕЛЬ 5: Container Scanning (Устаревший базовый образ)
# Trivy найдет сотни уязвимостей системного уровня (в Debian/Ubuntu) внутри этого образа.
FROM python:3.7-slim

WORKDIR /app

# 🎯 ЦЕЛЬ 6: Расширение поверхности атаки
# Уязвимость: Установка утилит, которые не нужны приложению, но очень полезны хакеру при взломе (netcat, curl).
RUN apt-get update && apt-get install -y netcat-openbsd curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🎯 ЦЕЛЬ 7: Container Scanning (Запуск от root)
# Уязвимость: По умолчанию Docker запускает процесс от имени суперпользователя. 
# Сканеры конфигураций (Trivy/Checkov) потребуют добавить инструкцию USER <non-root>.
EXPOSE 5000
CMD ["python", "app.py"]