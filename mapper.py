from openai import OpenAI
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("Add_your_API_Key"))

def generate_semantic_embeddings(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]

def enrich_with_embeddings(df):
    semantic_info = {}
    for col in df.columns:
        # Sample from the column to capture meaning
        sample_values = df[col].dropna().astype(str).tolist()[:5]
        text_input = [col] + sample_values
        embeddings = generate_semantic_embeddings(text_input)
        semantic_info[col] = np.mean(embeddings, axis=0) 
    return semantic_info
