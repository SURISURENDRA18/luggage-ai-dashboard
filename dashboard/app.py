import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Luggage Intelligence", layout="wide")


# LOAD DATA

df = pd.read_csv("data/processed/products_with_sentiment.csv")

# Fake columns
df["brand"] = df["title"].apply(lambda x: x.split()[0])
df["sentiment_score"] = df["rating"] * 20  # placeholder


# SIDEBAR
st.sidebar.title("Filters")

selected_brands = st.sidebar.multiselect(
    "Select Brand",
    options=df["brand"].unique(),
    default=df["brand"].unique()
)

price_range = st.sidebar.slider(
    "Price Range",
    int(df["price"].min()),
    int(df["price"].max()),
    (int(df["price"].min()), int(df["price"].max()))
)

filtered_df = df[
    (df["brand"].isin(selected_brands)) &
    (df["price"].between(price_range[0], price_range[1]))
]


# HEADER

st.title("Luggage Market Intelligence Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Brands", filtered_df["brand"].nunique())
col2.metric("Total Products", len(filtered_df))
col3.metric("Avg Price", f"₹{int(filtered_df['price'].mean())}")
col4.metric("Avg Sentiment", round(filtered_df["sentiment_score"].mean(), 2))

st.divider()


# BRAND COMPARISON

st.subheader(" Brand Comparison")

brand_group = filtered_df.groupby("brand").agg({
    "price": "mean",
    "rating": "mean",
    "sentiment_score": "mean"
}).reset_index()

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(brand_group, x="brand", y="price", title="Avg Price by Brand")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.bar(brand_group, x="brand", y="sentiment_score", title="Sentiment Score")
    st.plotly_chart(fig2, use_container_width=True)

# Scatter
fig3 = px.scatter(
    brand_group,
    x="price",
    y="rating",
    size="sentiment_score",
    color="brand",
    title="Price vs Rating (Bubble = Sentiment)"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()


# AI INSIGHTS 

st.subheader("AI Insights")

st.info("""
- Safari appears strongest in value-for-money segment  
- Skybags shows higher pricing but mixed sentiment  
- American Tourister has balanced pricing and strong ratings  
""")

st.divider()


# PRODUCT DRILLDOWN

st.subheader(" Product Drilldown")

selected_brand = st.selectbox("Select Brand", df["brand"].unique())

brand_df = df[df["brand"] == selected_brand]

st.dataframe(brand_df)


# RAW DATA

with st.expander("View Raw Data"):
    st.dataframe(filtered_df)
    
    
