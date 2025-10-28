import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("IExcludedMyAPIKey"))

def generate_schema(csv_path):
    df = pd.read_csv(csv_path)
    columns = list(df.columns)
    
    prompt = f"""
    You are a data-mapping agent. Given the following columns: {columns},
    infer the logical meaning for each field and produce a JSON schema
    with keys: 'column_name', 'description', and 'datatype'.
    Keep it concise and practical for business reporting.
    """
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    
    print("📘 AI Schema Suggestion:")
    print(response.output[0].content[0].text)

if __name__ == "__main__":
    generate_schema("sales.csv")
