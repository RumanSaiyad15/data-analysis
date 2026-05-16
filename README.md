# 📊 Online Store Analytics Dashboard

## Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## Features ✨

✅ **Single Page Dashboard** - All analytics on one screen
✅ **Professional Design** - Modern gradient UI with smooth animations
✅ **Interactive Charts** - Chart.js powered visualizations
✅ **KPI Cards** - Key business metrics at a glance
✅ **Responsive** - Works on desktop, tablet, and mobile
✅ **Real-time Data** - Reads from your CSV file

---

## Dashboard Sections 📈

1. **KPI Cards** - Quick overview of key metrics
   - Total Revenue
   - Total Orders
   - Unique Customers
   - Average Order Value
   - Pending Orders
   - Most Expensive Product

2. **Popular Products** - Top 3 best-selling products
3. **Payment Methods** - Distribution of payment types
4. **Order Status** - Shipped, Pending, Cancelled, Returned
5. **Top Customers** - Top 5 customers by order count
6. **Orders by City** - Top 10 cities with most orders

---

## File Structure

```
data analyze/
├── app.py                  # Flask application
├── data_analysis.py        # Original analysis script
├── Online-Store-Orders.csv # Data source
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html         # Dashboard HTML
```

---

## Customization

Edit the KPI cards and charts in `templates/index.html` to customize colors, layout, and metrics.

Modify data calculations in `app.py` to add more analysis or change existing metrics.

