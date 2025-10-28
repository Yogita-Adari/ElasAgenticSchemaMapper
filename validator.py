from db import get_connection
import json
import pandas as pd

def validate_schema(ai_schema_json, table_name):
    conn = get_connection()
    query = f"""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = '{table_name}'
    """
    df = pd.read_sql(query, conn)
    conn.close()

    ai_schema = json.loads(ai_schema_json)
    mismatches = []

    for col in ai_schema:
        db_match = df[df['column_name'] == col['column_name']]
        if db_match.empty:
            mismatches.append(f"Missing in DB: {col['column_name']}")
        elif db_match.iloc[0]['data_type'] not in col['datatype']:
            mismatches.append(f"Type mismatch for {col['column_name']}")

    if mismatches:
        print("⚠ Schema mismatches detected:")
        for m in mismatches:
            print(" -", m)
    else:
        print("✅ AI schema perfectly matches database table.")

