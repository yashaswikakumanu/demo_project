import json
import openai

HEALTH_LOG_FILE = "health_logs.json"

# Predefined conditions for health warnings
RISK_CONDITIONS = {
    "high_blood_pressure": "Blood Pressure above 140/90",
    "low_oxygen": "Oxygen level below 90%",
    "high_glucose": "Glucose level above 180 mg/dL",
}

def check_health_risks():
    """Check user logs for potential health risks"""
    try:
        with open(HEALTH_LOG_FILE, "r") as file:
            logs = json.load(file)
    except FileNotFoundError:
        return {"message": "No health data found."}

    alerts = []
    for log in logs:
        if "blood_pressure" in log and log["blood_pressure"] > 140:
            alerts.append(f"🚨 High Blood Pressure detected: {log['blood_pressure']}")
        if "oxygen_level" in log and log["oxygen_level"] < 90:
            alerts.append(f"⚠️ Low Oxygen Level: {log['oxygen_level']}%")
        if "glucose" in log and log["glucose"] > 180:
            alerts.append(f"⚠️ High Glucose Level: {log['glucose']} mg/dL")

    return {"alerts": alerts if alerts else "✅ No health risks detected."}
