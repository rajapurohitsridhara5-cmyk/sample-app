import os, json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print(json.dumps({"severity": "INFO", "message": "request received"}))
    return "Hello from DevOps prep v1\n"

@app.route("/healthz")
def health():
    return "ok\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
