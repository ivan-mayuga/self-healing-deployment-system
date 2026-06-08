import time
import requests
import subprocess
from datetime import datetime

from notifier import notify

URL = "http://localhost:5000/health"

service_was_down = False


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/monitor.log", "a") as log:
        log.write(f"{timestamp} - {message}\n")


while True:
    try:
        response = requests.get(URL, timeout=5)

        if response.status_code != 200:
            raise Exception("Health endpoint failed")

        print("Service healthy")
        log_event("HEALTHY")

        service_was_down = False

    except Exception as e:

        if not service_was_down:

            print("Service unhealthy")

            notify(f"Service failure detected: {e}")

            log_event("UNHEALTHY")

            subprocess.run(
                [
                    "python3",
                    "monitor/incident_report.py",
                    str(e)
                ]
            )

            subprocess.run(
                [
                    "docker",
                    "restart",
                    "myapp"
                ]
            )

            notify("Application restarted automatically")

            log_event("RESTARTED")

            service_was_down = True

    time.sleep(30)