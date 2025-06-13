import os
import time
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Configuración desde variables de entorno
APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "desconocido")
BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend-service:8080")

# Template HTML
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frontend App - {{ environment }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; }
        .container { max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); }
        .status { padding: 10px; margin: 10px 0; border-radius: 5px; background: rgba(255,255,255,0.2); }
        .healthy { background: rgba(76, 175, 80, 0.3); }
        .error { background: rgba(244, 67, 54, 0.3); }
    </style>
</head>
<body>
<div class="container">
    <h1>Aplicación Frontend</h1>
    <div class="status">
        <h3>Información del Sistema</h3>
        <p><strong>Versión:</strong> {{ version }}</p>
        <p><strong>Entorno:</strong> {{ environment }}</p>
        <p><strong>Timestamp:</strong> {{ timestamp }}</p>
    </div>
    <div class="status healthy">
        <h3>Estado del Servicio</h3>
        <p>Frontend funcionando correctamente</p>
    </div>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        version=APP_VERSION,
        environment=ENVIRONMENT,
        timestamp=time.strftime('%Y-%m-%d %H:%M:%S')
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

@app.route('/ready')
def ready():
    # En un caso real, aquí se verificarían las dependencias (ej. conexión al backend)
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    print(f"Iniciando Frontend App v{APP_VERSION} en entorno {ENVIRONMENT}")
    app.run(host='0.0.0.0', port=8080)