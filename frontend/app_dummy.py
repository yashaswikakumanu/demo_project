import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

# Sidebar Navigation
st.sidebar.title("Navigation")
choice = st.sidebar.selectbox("Choose an option:", 
                              ["Medical Report Summarization", 
                               "Track Your Health", 
                               "Health Alerts", 
                               "Adaptive AI Recommendations"])

# 📝 Medical Report Summarization
if choice == "Medical Report Summarization":
    st.title("📄 Medical Report Summarization")

    uploaded_file = st.file_uploader("Upload Medical Report", type=["pdf"])
    if uploaded_file:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{API_BASE}/upload/", files=files)
        if response.status_code == 200:
            st.write("📝 Summary:", response.json()["summary"])
        else:
            st.error("Error processing the file!")

# 📊 Track Your Health
elif choice == "Track Your Health":
    st.title("🏥 Track Your Health")

    user_id = st.text_input("User ID")
    food = st.text_input("🍎 Food Intake")
    steps = st.number_input("🚶 Steps Taken", min_value=0)

    if st.button("Log Entry"):
        data = {"user_id": user_id, "food": food, "steps": steps}
        response = requests.post(f"{API_BASE}/log/", json=data)
        if response.status_code == 200:
            st.success("✅ Entry logged successfully!")
        else:
            st.error("Failed to log entry.")

    if st.button("View Past Logs"):
        response = requests.get(f"{API_BASE}/logs/?user_id={user_id}")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error("No logs found.")

# 🚨 AI-Powered Health Alerts
elif choice == "Health Alerts":
    st.subheader("🚨 AI-Powered Health Alerts")
    
    response = requests.get(f"{API_BASE}/monitoring/")
    if response.status_code == 200:
        alerts = response.json()["alerts"]
        if isinstance(alerts, list):
            for alert in alerts:
                st.warning(alert)
        else:
            st.success(alerts)
    else:
        st.error("Error fetching health alerts!")

# 🔍 AI-Powered Personalized Recommendations
elif choice == "Adaptive AI Recommendations":
    st.subheader("🔍 AI-Powered Personalized Recommendations")
    
    response = requests.get(f"{API_BASE}/adaptive_recommendations/")
    if response.status_code == 200:
        recommendations = response.json()["adaptive_recommendations"]
        st.write(recommendations)
    else:
        st.error("Error fetching AI recommendations!")
