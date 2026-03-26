import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ultimate Sales Intelligence", layout="wide", page_icon="💎")

# --- CUSTOM CSS (NEON GLASS DESIGN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .stApp {
        background: radial-gradient(circle at top left, #0e1117, #010409);
        color: #e6edf3;
    }
    
    /* Custom Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 15px 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: 0.3s;
    }
    div[data-testid="stMetric"]:hover {
        border: 1px solid #00d4ff;
        transform: translateY(-5px);
    }
    
    /* Buttons and Inputs */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(45deg, #00d4ff, #0055ff);
        color: white;
        border: none;
        font-weight: bold;
    }
    
    /* Sidebar Design */
    [data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    .status-badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        border: 1px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ADVANCED DATA GENERATION ---
@st.cache_data
def get_data():
    np.random.seed(42)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    regions = ["North America", "Europe", "Asia-Pacific", "Latin America"]
    categories = ["Electronics", "Cloud Services", "Hardware", "Consulting"]
    
    rows = []
    for m in months:
        for r in regions:
            sales = np.random.randint(20000, 80000)
            expenses = np.random.randint(10000, 40000)
            rows.append({
                "Month": m,
                "Region": r,
                "Category": np.random.choice(categories),
                "Sales": sales,
                "Expenses": expenses,
                "Profit": sales - expenses,
                "Units": np.random.randint(100, 1000),
                "Satisfaction": np.random.uniform(3.5, 5.0)
            })
    return pd.DataFrame(rows)

df = get_data()

# --- SIDEBAR FILTERS ---
st.sidebar.title("💎 COMMAND CENTER")
st.sidebar.markdown("---")
selected_regions = st.sidebar.multiselect("Focus Regions", df["Region"].unique(), default=df["Region"].unique())
selected_cats = st.sidebar.multiselect("Product Categories", df["Category"].unique(), default=df["Category"].unique())

st.sidebar.markdown("### 🎯 Profit Simulator")
growth_rate = st.sidebar.slider("Projected Sales Growth (%)", 0, 50, 10)
cost_reduction = st.sidebar.slider("Expense Reduction (%)", 0, 50, 5)

# Filter logic
filtered_df = df[(df["Region"].isin(selected_regions)) & (df["Category"].isin(selected_cats))]

# --- HEADER ---
c1, c2 = st.columns([3, 1])
with c1:
    st.title("Enterprise Analytics OS")
    st.markdown('<span class="status-badge">SYSTEM ACTIVE</span> <span style="margin-left:10px; color:#8b949e;">Real-time Market Intelligence</span>', unsafe_allow_html=True)
with c2:
    st.markdown(f"**Current Date**\n{datetime.now().strftime('%B %d, %Y')}")

st.divider()

# --- TOP KPI ROW ---
k1, k2, k3, k4 = st.columns(4)
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
avg_sat = filtered_df["Satisfaction"].mean()
total_units = filtered_df["Units"].sum()

k1.metric("Total Revenue", f"${total_sales:,.0f}", delta="+12.5% YoY")
k2.metric("Net Profit", f"${total_profit:,.0f}", delta="+8.2% YoY")
k3.metric("Customer Score", f"{avg_sat:.2f} / 5.0", delta="+0.4")
k4.metric("Units Dispatched", f"{total_units:,}", delta="-2.1%")

# --- TABS SYSTEM ---
tab_overview, tab_deepdive, tab_whatif, tab_raw = st.tabs(["📊 Performance", "🗺️ Market Map", "🔮 Forecasting", "📋 Inventory"])

# --- TAB 1: PERFORMANCE ---
with tab_overview:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("Revenue vs Expenses Trend")
        # Interactive Multi-Line Chart
        trend_data = filtered_df.groupby("Month").agg({"Sales":"sum", "Expenses":"sum"}).reindex(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(x=trend_data.index, y=trend_data["Sales"], name="Sales", line=dict(color='#00d4ff', width=4), mode='lines+markers'))
        fig_trend.add_trace(go.Scatter(x=trend_data.index, y=trend_data["Expenses"], name="Expenses", line=dict(color='#ff4b4b', width=2, dash='dash')))
        fig_trend.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with col_right:
        st.subheader("Regional Leaderboard")
        reg_leader = filtered_df.groupby("Region")["Sales"].sum().sort_values(ascending=True)
        fig_reg = px.bar(reg_leader, orientation='h', color=reg_leader.values, color_continuous_scale='Blues')
        fig_reg.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, height=400)
        st.plotly_chart(fig_reg, use_container_width=True)

# --- TAB 2: MARKET MAP ---
with tab_deepdive:
    c_a, c_b = st.columns(2)
    with c_a:
        st.subheader("Sales Treemap (Region > Category)")
        fig_tree = px.treemap(filtered_df, path=['Region', 'Category'], values='Sales', color='Profit', color_continuous_scale='RdYlGn')
        fig_tree.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_tree, use_container_width=True)
    
    with c_b:
        st.subheader("Profitability Gauge")
        margin = (total_profit / total_sales) * 100
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = margin,
            title = {'text': "Avg Profit Margin %"},
            gauge = {'axis': {'range': [None, 100]},
                     'bar': {'color': "#00d4ff"},
                     'steps' : [
                         {'range': [0, 20], 'color': "#ff4b4b"},
                         {'range': [20, 50], 'color': "#ffa500"},
                         {'range': [50, 100], 'color': "#00ff00"}]}))
        fig_gauge.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', height=400)
        st.plotly_chart(fig_gauge, use_container_width=True)

# --- TAB 3: WHAT-IF ANALYSIS (UNIQUE) ---
with tab_whatif:
    st.subheader("🚀 Profit Growth Simulator")
    st.write("Adjust the sidebar sliders to see how growth and cost-cutting affect your bottom line.")
    
    simulated_sales = total_sales * (1 + growth_rate/100)
    simulated_expenses = (filtered_df["Expenses"].sum()) * (1 - cost_reduction/100)
    simulated_profit = simulated_sales - simulated_expenses
    
    sc1, sc2, sc3 = st.columns(3)
    sc1.metric("Projected Sales", f"${simulated_sales:,.0f}")
    sc2.metric("Projected Expenses", f"${simulated_expenses:,.0f}")
    sc3.metric("Projected Net Gain", f"${simulated_profit:,.0f}", delta=f"{(simulated_profit-total_profit):,.0f} gain")
    
    # AI Insight Logic
    st.info(f"💡 **AI Insight:** Increasing your growth to {growth_rate}% while cutting costs by {cost_reduction}% will result in a **{((simulated_profit/total_profit)-1)*100:.1f}% increase** in total net profit.")

# --- TAB 4: RAW DATA ---
with tab_raw:
    st.subheader("Advanced Data Filtering")
    # Search Bar
    search = st.text_input("🔍 Search Transactions (e.g. 'Electronics' or 'Jan')")
    
    # Final data display
    display_df = filtered_df.copy()
    if search:
        display_df = display_df[display_df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
    
    st.dataframe(display_df.style.background_gradient(cmap='Blues', subset=['Sales', 'Profit']), use_container_width=True)
    
    # Download Button
    csv = display_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Export Current View to CSV", data=csv, file_name="sales_export.csv", mime="text/csv")

# --- FOOTER ---
st.markdown("---")
f1, f2, f3 = st.columns(3)
with f1: st.caption("© 2024 Analytics Corp | v4.0.2")
with f2: st.caption("Data Source: Simulated Enterprise ERP")
with f3: 
    if st.button("🔄 Refresh Live Stream"):
        st.toast("Syncing with Global Servers...")
        st.rerun()
