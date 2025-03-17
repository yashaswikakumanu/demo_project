import streamlit as st
import requests

st.title("AI-Powered Medical History & Health Tracker")

menu = ["Summarize Report", "Log Health Data", "View Recommendations", "Chat with AI"]
choice = st.sidebar.selectbox("Select Feature", menu)

API_BASE = "http://localhost:8000"

if choice == "Summarize Report":
    st.subheader("Upload Medical Report")
    file = st.file_uploader("Choose a PDF file", type=["pdf"])
    
    if st.button("Summarize"):
        with open("uploaded_report.pdf", "wb") as f:
            f.write(file.read())

        response = requests.post(f"{API_BASE}/summarize/", json={"file_path": "uploaded_report.pdf"})
        st.success(response.json())

elif choice == "Log Health Data":
    st.subheader("Enter Health Data")
    activity = st.text_input("Activity (e.g., Ate Salad, Walked 5km)")
    date = st.date_input("Date")

    if st.button("Log Entry"):
        response = requests.post(f"{API_BASE}/log_health/", json={"date": str(date), "activity": activity})
        st.success(response.json()["message"])

elif choice == "View Recommendations":
    st.subheader("AI-Powered Health Recommendations")
    response = requests.get(f"{API_BASE}/recommendations/")
    st.write(response.json()["recommendations"])

elif choice == "Chat with AI":
    st.subheader("Ask AI about your health")
    user_input = st.text_input("Your question:")
    
    if st.button("Ask AI"):
        response = requests.post(f"{API_BASE}/chat/", json={"message": user_input})
        st.write(response.json()["response"])
