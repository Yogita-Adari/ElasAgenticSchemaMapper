from fastapi import FastAPI, UploadFile
import pandas as pd
import io
from mapper import generate_schema
app = FastAPI()

@app.post("/infer-schema")
async def infer_schema(file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    schema = generate_schema(df)
    return {"inferred_schema": schema}

@app.get("/")
def home():
    return {"message": "ElasMapper API running!"}
