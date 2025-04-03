import streamlit as st
import pandas as pd
import plotly.express as px
import nltk
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

# Download NLTK data (only if needed)
nltk.download('punkt')

# Load dataset
df = pd.read_csv("hackathon_dataset.csv")

# Page Title
st.title("📝 Text Analysis of Participant Feedback")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
selected_domain = st.sidebar.selectbox("Select Domain", ["All"] + list(df["Domain"].unique()))

# Apply Domain Filter
filtered_df = df.copy()
if selected_domain != "All":
    filtered_df = filtered_df[filtered_df["Domain"] == selected_domain]

# Word Cloud for All Feedback
st.subheader("📌 Word Cloud for Participant Feedback")
all_feedback = " ".join(filtered_df["Feedback"].dropna())

if all_feedback:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_feedback)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("No feedback available for selected filters.")

# Domain-wise Feedback Comparison
st.subheader("🔍 Domain-wise Feedback Distribution")
domain_feedback = filtered_df.groupby("Domain")["Feedback"].count().reset_index()
domain_chart = px.bar(domain_feedback, x="Domain", y="Feedback", color="Domain", title="Feedback Count per Domain")
st.plotly_chart(domain_chart, use_container_width=True)

# # Sentiment Analysis
# st.subheader("📊 Sentiment Analysis of Feedback")

# def get_sentiment(text):
#     analysis = TextBlob(text)
#     if analysis.sentiment.polarity > 0:
#         return "Positive"
#     elif analysis.sentiment.polarity < 0:
#         return "Negative"
#     else:
#         return "Neutral"

# filtered_df["Sentiment"] = filtered_df["Feedback"].apply(get_sentiment)
# sentiment_counts = filtered_df["Sentiment"].value_counts().reset_index()
# sentiment_chart = px.pie(sentiment_counts, names="index", values="Sentiment", title="Overall Sentiment Analysis")
# st.plotly_chart(sentiment_chart, use_container_width=True)

# Sentiment Analysis
st.subheader("📊 Sentiment Analysis of Feedback")

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

filtered_df["Sentiment"] = filtered_df["Feedback"].apply(get_sentiment)

# Get sentiment counts
sentiment_counts = filtered_df["Sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "count"]  # Rename columns to make it easier to plot

# Plot sentiment pie chart
sentiment_chart = px.pie(sentiment_counts, names="Sentiment", values="count", title="Overall Sentiment Analysis")
st.plotly_chart(sentiment_chart, use_container_width=True)

