import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")

np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = {
    "Month": months,
    "Sales": np.random.randint(10000, 50000, 12),
    "Expenses": np.random.randint(5000, 30000, 12),
    "Units Sold": np.random.randint(100, 500, 12),
    "Region": ["North", "South", "East", "West"] * 3
}

df = pd.DataFrame(data)
df["Profit"] = df["Sales"] - df["Expenses"]

st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())

filtered = df[df["Region"].isin(selected_region)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered['Sales'].sum():,}")
col2.metric("Total Expenses", f"${filtered['Expenses'].sum():,}")
col3.metric("Net Profit", f"${filtered['Profit'].sum():,}")

st.subheader("Monthly Sales vs Expenses")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered["Month"], filtered["Sales"], marker="o", label="Sales", color="#4CAF50")
ax.plot(filtered["Month"], filtered["Expenses"], marker="s", label="Expenses", color="#F44336")
ax.fill_between(filtered["Month"], filtered["Sales"], filtered["Expenses"], alpha=0.1, color="blue")
ax.legend()
ax.set_xlabel("Month")
ax.set_ylabel("Amount ($)")
plt.xticks(rotation=45)
st.pyplot(fig)

col4, col5 = st.columns(2)

with col4:
    st.subheader("Profit by Month")
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    colors = ["#4CAF50" if p > 0 else "#F44336" for p in filtered["Profit"]]
    ax2.bar(filtered["Month"], filtered["Profit"], color=colors)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Profit ($)")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

with col5:
    st.subheader("Sales by Region")
    region_data = filtered.groupby("Region")["Sales"].sum()
    fig3, ax3 = plt.subplots(figsize=(5, 4))
    ax3.pie(region_data, labels=region_data.index, autopct="%1.1f%%", startangle=90)
    st.pyplot(fig3)

st.subheader("Raw Data")
st.dataframe(filtered, use_container_width=True)
