import os
import time
import random
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "desconocido")
DATABASE_URL = os.environ.get("DATABASE_URL", "not-set")

@app.route('/')
def home():
    return jsonify({
        "service": "backend-api",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "message": "Backend API funcionando correctamente"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

@app.route('/ready')
def ready():
    # En un caso real, verificar la conexión a la base de datos
    return jsonify({"status": "ready", "database_url": DATABASE_URL}), 200

@app.route('/api/users')
def get_users():
    return jsonify([
        {"id": 1, "name": "Juan Pérez", "email": "juan@example.com"},
        {"id": 2, "name": "María García", "email": "maria@example.com"},
    ])

if __name__ == '__main__':
    print(f"Iniciando Backend API v{APP_VERSION} en entorno {ENVIRONMENT}")
    app.run(host='0.0.0.0', port=8080)