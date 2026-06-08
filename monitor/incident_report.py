import json
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path("reports")

REPORTS_DIR.mkdir(exist_ok=True)

def create_report(reason):
    report = {
        "timestamp": datetime.now().isoformat(),
        "service": "myapp",
        "failure_reason": reason,
        "action": "rollback initiated"
    }

    filename = REPORTS_DIR / f"incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"Incident report created: {filename}")

if __name__ == "__main__":
    import sys
    create_report(sys.argv[1])