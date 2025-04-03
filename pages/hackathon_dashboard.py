import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("hackathon_dataset.csv")

# Streamlit Page Config
st.set_page_config(page_title="Hackathon Event Dashboard", layout="wide")

# Title
st.title("📊 Hackathon Event Analysis Dashboard")

st.sidebar.success("Select a page above ⬆️")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
selected_domain = st.sidebar.selectbox("Select Domain", ["All"] + list(df["Domain"].unique()))
selected_state = st.sidebar.selectbox("Select State", ["All"] + list(df["State"].unique()))
selected_college = st.sidebar.selectbox("Select College", ["All"] + list(df["College"].unique()))

# Apply Filters
filtered_df = df.copy()
if selected_domain != "All":
    filtered_df = filtered_df[filtered_df["Domain"] == selected_domain]
if selected_state != "All":
    filtered_df = filtered_df[filtered_df["State"] == selected_state]
if selected_college != "All":
    filtered_df = filtered_df[filtered_df["College"] == selected_college]

# Display Summary
st.write(f"### Total Participants: {filtered_df.shape[0]}")

# Charts
col1, col2 = st.columns(2)

# Domain-wise Distribution
domain_chart = px.bar(df, x="Domain", title="📌 Participants by Domain", color="Domain")
col1.plotly_chart(domain_chart, use_container_width=True)

# Day-wise Participation
day_chart = px.pie(df, names="Day", title="📅 Participation by Day")
col2.plotly_chart(day_chart, use_container_width=True)

# College-wise Participation
college_chart = px.bar(df, x="College", title="🏫 Participation by College", color="College")
st.plotly_chart(college_chart, use_container_width=True)

# State-wise Participation
state_chart = px.bar(df, x="State", title="📍 Participation by State", color="State")
st.plotly_chart(state_chart, use_container_width=True)

# Run Streamlit App
# In terminal: streamlit run hackathon_dashboard.py
