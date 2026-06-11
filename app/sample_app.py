import os
import time

from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency"
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Application Running - Version 2"


@app.route("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "healthy"}


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": "text/plain"
    }


@app.before_request
def start_timer():
    app.start_time = time.time()


@app.after_request
def record_latency(response):
    if hasattr(app, "start_time"):
        REQUEST_LATENCY.observe(
            time.time() - app.start_time
        )
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
