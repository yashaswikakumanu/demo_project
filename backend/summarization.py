import pdfplumber
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def summarize_medical_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a medical assistant simplifying medical reports for patients."},
                  {"role": "user", "content": f"Summarize this in layman's terms:\n{text}"}],
                  max_tokens=100
    )
    return response['choices'][0]['message']['content']
