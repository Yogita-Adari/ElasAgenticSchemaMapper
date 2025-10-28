# ElasAgenticSchemaMapper

ElasMapper (ElasAgenticSchemaMapper) is a lightweight **agentic AI system** that automatically analyzes and maps the structure of raw CSV data into meaningful database schemas.  
It bridges traditional data pipelines with AI reasoning to make schema detection, metadata inference, and data onboarding faster and more context-aware.

---

## Introduction

This project demonstrates a full end-to-end workflow:

1. **Data Upload** — CSV files (e.g., sales, customers, employees) are uploaded through a FastAPI interface.  
2. **Database Integration** — PostgreSQL acts as the storage engine for scalable and persistent data handling.  
3. **AI Schema Inference** — The Agentic AI pipeline analyzes uploaded data, infers field meanings, and generates a JSON schema containing column names, logical descriptions, and datatypes.  
4. **Live API Response** — The results are returned through a clean REST endpoint (`/infer-schema`), viewable in the browser or via API clients like Thunder Client or Postman.

---
Architectural Layer for Semantic Matching 
<img width="1004" height="640" alt="image" src="https://github.com/user-attachments/assets/c1fe510e-c163-45d6-9b0a-52d1e78cced6" />

---

## Technologies used

- **FastAPI** – lightweight RESTful framework  
- **PostgreSQL** – robust database backend  
- **OpenAI GPT-based Agentic AI** – for schema reasoning and data interpretation  
- **Python** – using `pandas`, `sqlalchemy`, and `dotenv` for orchestration  
- **Uvicorn** – async server for API hosting  

---
## Example Input

Sales.csv 
<img width="1132" height="356" alt="image" src="https://github.com/user-attachments/assets/8bdeb1df-8fe6-4f39-899b-84a06b8d22fe" />

## Example output

When the server runs successfully (`http://127.0.0.1:8000`), the home endpoint returns:

```json
{
  "message": "ElasMapper API running!"
}
