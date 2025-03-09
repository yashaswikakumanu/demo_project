import streamlit as st
import requests

st.title("Medical History Tracker")

uploaded_file = st.file_uploader("Upload Medical Report", type=["pdf"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/upload/", files=files)
    if response.status_code == 200:
        st.write("Summary:", response.json()["summary"])

st.header("Track Your Health")
user_id = st.text_input("User ID")
food = st.text_input("Food Intake")
steps = st.number_input("Steps Taken", min_value=0)
if st.button("Log Entry"):
    data = {"user_id": user_id, "food": food, "steps": steps}
    response = requests.post("http://127.0.0.1:8000/log/", json=data)
    if response.status_code == 200:
        st.success("Entry logged!")

if st.button("View Past Logs"):
    response = requests.get(f"http://127.0.0.1:8000/logs/?user_id={user_id}")
    if response.status_code == 200:
        st.write(response.json())
