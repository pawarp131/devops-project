from flask import Flask, jsonify, render_template_string
from datetime import datetime
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")
ENV = os.getenv("ENV", "dev")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>🚀 DevOps Application</h1>
    <p><b>Version:</b> {{ version }}</p>
    <p><b>Environment:</b> {{ env }}</p>
    <p><b>Deployed At:</b> {{ time }}</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        version=APP_VERSION,
        env=ENV,
        time=datetime.now()
    )

@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "time": str(datetime.now())
    })

@app.route('/version')
def version():
    return jsonify({
        "version": APP_VERSION,
        "environment": ENV
    })

@app.route('/metrics')
def metrics():
    return jsonify({
        "uptime": "running",
        "requests": "N/A (basic app)",
        "timestamp": str(datetime.now())
    })

if __name__ == "__main__":
    print(f"Starting app version {APP_VERSION} in {ENV} environment")
    app.run(host="0.0.0.0", port=5000)
