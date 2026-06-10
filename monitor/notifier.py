import os
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def notify(message):
    print(f"[ALERT] {message}")

    if not DISCORD_WEBHOOK_URL:
        print("[WARNING] Discord webhook URL not configured.")
        return

    payload = {
        "content": f"🚨 **SELF-HEALING SYSTEM ALERT**\n\n{message}"
    }

    try:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            timeout=10
        )

        if response.status_code not in (200, 204):
            print(
                f"[ERROR] Failed to send Discord alert: "
                f"{response.status_code} {response.text}"
            )

    except Exception as e:
        print(f"[ERROR] Discord notification failed: {e}")