import os
import pandas as pd
from textblob import TextBlob


def analyze_sentiment(text):
    text = str(text)

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


def run_sentiment():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, "data", "processed", "products_clean.csv")
    output_path = os.path.join(base_dir, "data", "processed", "products_with_sentiment.csv")

    df = pd.read_csv(input_path)

    df["sentiment_analysis"] = df["title"].apply(analyze_sentiment)

    df.to_csv(output_path, index=False)

    print("Sentiment fixed (no API errors)")


if __name__ == "__main__":
    run_sentiment()