from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Application Running"

@app.route("/health")
def health():
    return {"status": "healthy"}

app.run(host="0.0.0.0", port=5000)