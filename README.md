# � Ultimate Sales Intelligence

A dynamic enterprise sales analytics dashboard built with Streamlit.
The app generates simulated monthly sales data and provides interactive filtering, KPIs, visualizations, forecasting, and CSV export.

---

## Tech Stack

- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Plotly

---

## App Features

- Synthetic dataset generation (monthly sales by region, category, profit, units, satisfaction)
- Sidebar filters: regions and product categories
- Profit simulator with adjustable projected growth and expense reduction
- KPI cards for revenue, profit, satisfaction score, and units
- Multi-tab analytics:
  - Performance trend (line chart + regional bar chart)
  - Market map (treemap + profitability gauge)
  - What-if forecast projections
  - Raw filtered data with live search and CSV export
- Custom neon-glass UI styling and responsive layout

---

## Requirements

Make sure to install dependencies (see `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
streamlit run app.py
```

Open in browser at `http://localhost:8501`.

---

## Project Structure

```
capstone project/
├── app.py
├── requirements.txt
└── README.md
```

---

## Notes

- Data is generated in-memory at startup (`@st.cache_data` for performance).
- The app currently uses simulated ERP dataset; replace `get_data()` for real input sources.
- The footer includes refresh logic and system status indicators.

