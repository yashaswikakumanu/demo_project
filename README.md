# Medical History Summarization App  

## Overview  
The **Medical History Summarization App** is an AI-powered application that simplifies complex medical reports into easy-to-understand summaries.  
It extracts text from medical PDFs and uses **GPT-4o Mini** (OpenAI API) for summarization.  

---

## Features  
1. Extracts text from medical PDF reports 
2. Uses **GPT-4o Mini** (OpenAI API) for summarization 
3. Converts medical jargon into simple explanations 🏷️  
4. Provides an API for seamless integration 🔗  

---

## Tech Stack  
- **Backend**: FastAPI (Python)  
- **AI Models**: OpenAI GPT-4o Mini 
- **Libraries**:  
  - `openai` (for OpenAI API)  
  - `pdfplumber` (for extracting text from PDFs)  
  - `uvicorn` (for running FastAPI server)  

---

## Setup Instructions  

### 1. Clone the Repository  
```sh
git clone https://github.com/your-username/medical-history-app.git
cd medical-history-app
```

### 2. Create a Virtual Environment 
```sh
python3 -m venv medical_app_env
source medical_app_env/bin/activate  # Mac/Linux
medical_app_env\Scripts\activate  # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up API Keys
Create a .env file in the root directory and add:
```sh
OPENAI_API_KEY="your-openai-api-key"
```

### 5. Run the Application
```sh
uvicorn backend.main:app --reload
```



