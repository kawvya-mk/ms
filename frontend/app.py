
import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

API1_URL = os.getenv(
    "API1_URL", "http://localhost:5001/greet"
)
API2_URL = os.getenv(
    "API2_URL", "http://localhost:5002/info"
)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Microservices Application</title>
</head>
<body>
    <h1>Microservices Demo</h1>

    <h2>Greeting API</h2>
    <pre>{{ greeting }}</pre>

    <h2>Information API</h2>
    <pre>{{ information }}</pre>
</body>
</html>
"""

@app.route("/")
def home():
    try:
        response1 = requests.get(API1_URL, timeout=5)
        response1.raise_for_status()
        greeting = response1.json()
    except requests.RequestException as error:
        greeting = {"error": str(error)}

    try:
        response2 = requests.get(API2_URL, timeout=5)
        response2.raise_for_status()
        information = response2.json()
    except requests.RequestException as error:
        information = {"error": str(error)}

    return render_template_string(
        HTML,
        greeting=greeting,
        information=information
    )

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
