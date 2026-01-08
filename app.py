from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()[:12]  
    return render_template("index.html", message=f" 1 CI/CD test - [current env]  Task: {hostname}")

@app.route("/health")
def health():
    return "SUCCESS", 200

@app.route("/error")
def error():
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
