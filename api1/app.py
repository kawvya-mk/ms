
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"service": "API 1", "status": "running"})

@app.route("/greet")
def greet():
    return jsonify({
        "message": "Hello from API 1!",
        "service": "Greeting API"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
