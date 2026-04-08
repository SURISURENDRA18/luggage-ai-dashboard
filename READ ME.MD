Luggage Market Intelligence Dashboard
An AI-powered competitive intelligence dashboard that analyzes Amazon India luggage brands using real customer reviews, pricing data, and sentiment insights.

E-commerce platforms contain vast amounts of unstructured data, but extracting meaningful insights from reviews, pricing, and ratings remains challenging.

This project builds an end-to-end pipeline that:
	•	Collects product and review data
	•	Analyzes customer sentiment and themes
	•	Compares brands across key metrics
	•	Generates AI-driven insights
	•	Presents everything through an interactive dashboard

The goal is to enable data-driven decision-making for product positioning, pricing strategy, and customer perception.

⸻

🧠 System Architecture

Scraper → Data Processing → Sentiment Engine → Insight Agent → Dashboard

⸻

⚙️ Core Features

🔍 Data Collection
	•	Scrapes product listings and customer reviews from Amazon India
	•	Supports multiple luggage brands (e.g., Safari, Skybags, VIP, American Tourister)

🧹 Data Processing
	•	Cleans and structures raw data into analysis-ready format
	•	Standardizes price, rating, and review fields

🤖 Sentiment Analysis
	•	Classifies reviews as positive, negative, or neutral
	•	Extracts recurring themes such as durability, wheels, handle, and build quality

📊 Competitive Intelligence
	•	Compares brands based on:
	•	Average price
	•	Discount patterns
	•	Ratings and review volume
	•	Sentiment score

🧠 AI Insights (Key Differentiator)
	•	Automatically generates strategic insights, for example:
	•	“Brand A is overpriced relative to customer sentiment”
	•	“Brand B dominates the value-for-money segment”

🎛️ Interactive Dashboard
	•	KPI overview (brands, products, sentiment)
	•	Brand comparison visualizations
	•	Product-level drilldowns
	•	Dynamic filters (price, rating, brand)

⸻

📊 Dashboard Highlights
	•	KPI Summary: High-level metrics for quick understanding
	•	Brand Comparison: Price vs sentiment vs rating analysis
	•	AI Insights Panel: Automatically generated conclusions
	•	Product Drilldown: Detailed product-level insights
	•	Data Explorer: Access to processed dataset


    Run Pipeline

    python scraper/amazon_scraper.py:python scraper/amazon_scraper.py

    Clean data:python processing/clean_data.py

    Run sentiment analysis:python sentiment/sentiment_engine.py

    Launch dashboard:streamlit run dashboard/app.py

    Suri Surendra
AI Engineer | Agentic AI |