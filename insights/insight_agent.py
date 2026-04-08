import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_insights():
    df = pd.read_csv("data/processed/products_with_sentiment.csv")

    summary = df.describe().to_string()

    prompt = f"""
    Based on this dataset summary, generate 5 smart insights about:
    - pricing strategy
    - product quality
    - customer perception

    Data:
    {summary}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    generate_insights()
    
    