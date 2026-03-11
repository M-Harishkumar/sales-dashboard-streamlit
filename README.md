# 💸 Personal Expense Tracker

A simple expense tracking web app built with Streamlit. You can add expenses, view charts, filter by category, and export your data as CSV.

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib

---

## Features

- Add expenses with date, category, description, and amount
- Summary metrics — total spent, average, and top category
- Pie chart and bar chart breakdown by category
- Daily spending trend line chart
- Filter expenses by category
- Upload an existing CSV file
- Export your data back to CSV

---

## How to Run

**1. Clone or download the project**

```bash
git clone <your-repo-url>
cd expense-tracker
```

**2. Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## CSV Upload Format

If you want to load existing data, your CSV file should have these columns:

```
Date, Category, Description, Amount
2024-01-15, Food, Lunch, 150.00
2024-01-16, Transport, Bus fare, 30.00
```

---

## Project Structure

```
expense-tracker/
├── app.py
├── requirements.txt
└── README.md
```
