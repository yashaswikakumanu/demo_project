import json
import os

# File to store health data (simulating a database)
HEALTH_LOG_FILE = "health_logs.json"

# Ensure the file exists
if not os.path.exists(HEALTH_LOG_FILE):
    with open(HEALTH_LOG_FILE, "w") as f:
        json.dump({}, f)

def log_health_data(entry):
    try:
        with open(HEALTH_LOG_FILE, "r") as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(entry)

    with open(HEALTH_LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)
    
    return {"message": "Health data logged successfully!"}

def get_health_logs():
    try:
        with open(HEALTH_LOG_FILE, "r") as file:
            logs = json.load(file)
        return logs
    except:
        return {"error": "No health data found"}
