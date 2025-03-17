from fastapi import FastAPI, File, UploadFile
from backend.summarization import extract_text_from_pdf,summarize_medical_text
from backend.health_tracking import log_health_data, get_health_logs
# from backend.recommendations import get_health_recommendations
from backend.chatbot import chat_with_ai

app = FastAPI()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    summary = summarize_medical_text(text)
    return {"summary": summary}

@app.post("/log_health/")
async def log_health_entry(data: dict):
    return log_health_data(data)

@app.get("/health_logs/")
async def retrieve_health_logs():
    return get_health_logs()

# @app.get("/recommendations/")
# async def get_ai_recommendations():
#     return get_health_recommendations()

@app.post("/chat/")
async def chat_with_ai_agent(message: str):
    return chat_with_ai(message)

