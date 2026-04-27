import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("📊 Customer Churn Analysis Dashboard")

# -------------------------
# Load data
# -------------------------
summary = pd.read_csv("summary.csv")
contract = pd.read_csv("contract_churn.csv")
internet = pd.read_csv("internet_churn.csv")
tenure = pd.read_csv("tenure_analysis.csv")
charges = pd.read_csv("charges_analysis.csv")

# -------------------------
# KPI
# -------------------------
st.subheader("📉 Overall Churn Rate")
st.metric("Churn Rate (%)", round(summary["Value"][0], 2))

# -------------------------
# Contract Churn
# -------------------------
st.subheader("📄 Churn by Contract Type")
st.bar_chart(contract.set_index("Contract"))

# -------------------------
# Internet Service
# -------------------------
st.subheader("🌐 Churn by Internet Service")
st.bar_chart(internet.set_index("InternetService"))

# -------------------------
# Tenure
# -------------------------
st.subheader("⏳ Average Tenure (Churn vs No Churn)")
st.bar_chart(tenure.set_index("Churn"))

# -------------------------
# Charges
# -------------------------
st.subheader("💰 Monthly Charges (Churn vs No Churn)")
st.bar_chart(charges.set_index("Churn"))
