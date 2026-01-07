from flask import Flask, render_template
import threading
import time
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", message="Hello World!233333")

@app.route("/health")
def health():
    return "SUCCESS", 200


def delayed_crash():
    time.sleep(30)  # 30초 후 크래시
    os._exit(1)

# 앱 시작 시 백그라운드 스레드 실행
threading.Thread(target=delayed_crash, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
