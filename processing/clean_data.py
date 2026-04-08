import os
import pandas as pd

def clean_data():
    #Safe path handling
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "raw", "products.csv")
    processed_path = os.path.join(base_dir, "data", "processed", "products_clean.csv")

    #Ensure output directory exists
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)

    #Load data safely
    try:
        df = pd.read_csv(raw_path)
    except FileNotFoundError:
        print("Raw data file not found. Run scraper first.")
        return

    #Clean price (handle ₹, commas, missing values)
    if "price" in df.columns:
        df["price"] = (
            df["price"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)
        )
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    #Clean rating (handle different formats safely)
    if "rating" in df.columns:
        df["rating"] = df["rating"].astype(str).str.extract(r"(\d+\.?\d*)")
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    #Drop rows where important fields are missing
    df.dropna(subset=["price", "rating"], inplace=True)

    #Remove duplicates
    df.drop_duplicates(inplace=True)

    #Save cleaned data
    df.to_csv(processed_path, index=False)

    print(f" Data cleaned and saved to: {processed_path}")

if __name__ == "__main__":
    clean_data()
    
    