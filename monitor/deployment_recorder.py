import json
import os
from datetime import datetime

HISTORY_FILE = "deployments/deployment_history.json"

def record_deployment(status):
    deployment = {
        "timestamp": datetime.now().isoformat(),
        "status": status
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(deployment)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

if __name__ == "__main__":
    import sys
    record_deployment(sys.argv[1])