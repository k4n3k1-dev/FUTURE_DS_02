import pandas as pd

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("customer_churn.csv")

# -------------------------
# Clean data
# -------------------------
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# Convert churn to binary
df['ChurnFlag'] = df['Churn'].apply(lambda x: 1 if x == "Yes" else 0)

# -------------------------
# 1. Overall Churn Rate
# -------------------------
churn_rate = df['ChurnFlag'].mean() * 100

# -------------------------
# 2. Churn by Contract Type
# -------------------------
contract_churn = df.groupby('Contract')['ChurnFlag'].mean().reset_index()
contract_churn.to_csv("contract_churn.csv", index=False)

# -------------------------
# 3. Churn by Internet Service
# -------------------------
internet_churn = df.groupby('InternetService')['ChurnFlag'].mean().reset_index()
internet_churn.to_csv("internet_churn.csv", index=False)

# -------------------------
# 4. Tenure Analysis
# -------------------------
tenure_analysis = df.groupby('Churn')['tenure'].mean().reset_index()
tenure_analysis.to_csv("tenure_analysis.csv", index=False)

# -------------------------
# 5. Monthly Charges vs Churn
# -------------------------
charges_analysis = df.groupby('Churn')['MonthlyCharges'].mean().reset_index()
charges_analysis.to_csv("charges_analysis.csv", index=False)

# -------------------------
# Save churn summary
# -------------------------
summary = pd.DataFrame({
    "Metric": ["Churn Rate (%)"],
    "Value": [churn_rate]
})
summary.to_csv("summary.csv", index=False)

print("✅ Churn analysis completed successfully.")
