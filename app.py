from flask import Flask, render_template
import signal 
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", message="Hello World!")

@app.route("/health")
def health():
    return "SUCCESS", 200

@app.route("/crash")
def crash():
    """호출 시 컨테이너 강제 종료"""
    os.kill(1, signal.SIGKILL)
    return "crashing...", 200
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
