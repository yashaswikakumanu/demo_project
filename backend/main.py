from fastapi import FastAPI, File, UploadFile
from backend.summarization import extract_text_from_pdf, summarize_medical_text
from backend.health_tracking import log_health_data, get_past_logs
import uvicorn

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    summary = summarize_medical_text(text)
    return {"summary": summary}

@app.post("/log/")
async def log_data(user_id: str, food: str, steps: int):
    log_health_data(user_id, food, steps, "User daily log")
    return {"status": "Logged successfully"}

@app.get("/logs/")
async def fetch_logs(user_id: str):
    return get_past_logs(user_id)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
