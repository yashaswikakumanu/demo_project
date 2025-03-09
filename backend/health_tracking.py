import json
import os

# File to store health data (simulating a database)
DATA_FILE = "health_logs.json"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def log_health_data(user_id: str, food: str, steps: int, note: str):
    """Logs health data for a user."""
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({"food": food, "steps": steps, "note": note})

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_past_logs(user_id: str):
    """Retrieves past health logs for a user."""
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return data.get(user_id, [])
