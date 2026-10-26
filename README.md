# E-Commerce Sales Analysis | Python, PostgreSQL & Power BI

## Project Overview

This project focuses on analyzing e-commerce data to understand sales performance, customer purchasing behavior, product demand, order trends, and inventory levels.

The project combines **Python for data cleaning and exploratory data analysis (EDA)**, **PostgreSQL for SQL-based analysis**, and **Power BI for interactive dashboard development**.

The goal is to transform raw e-commerce data into meaningful business insights that support data-driven decision-making.

## Project Objectives

- Analyze overall order and sales performance.
- Identify popular products and product categories.
- Understand customer purchasing behavior.
- Analyze monthly delivered revenue trends.
- Monitor order status distribution.
- Identify low-stock products for inventory management.
- Build an interactive Power BI dashboard.

## Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Data analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| PostgreSQL | Database management and SQL analysis |
| pgAdmin 4 | PostgreSQL database administration |
| Power BI | Interactive dashboard development |
| DAX | KPI measures and calculations |
| VS Code | Development environment |
| GitHub | Version control and project documentation |

## Dataset Description

The project uses three CSV datasets containing approximately 1,000 records each.

| Dataset | Description |
|---|---|
| customers-1000.csv | Customer information and subscription details |
| orders-1000.csv | Order transactions, dates, quantities, status, and values |
| products-1000.csv | Product information, categories, pricing, ratings, and inventory |

The datasets are connected using customer and product identifiers.

## Project Workflow

### 1. Data Cleaning and Preparation

Performed data preparation using Python and Pandas.

- Loaded CSV datasets.
- Examined data types and dataset structure.
- Checked missing values and duplicate records.
- Converted date columns into appropriate datetime formats.
- Validated numerical and categorical columns.
- Prepared data for further analysis.

### 2. Exploratory Data Analysis (EDA)

Performed analysis using Pandas and Matplotlib to explore:

- Order status distribution
- Sales performance
- Customer purchasing patterns
- Top-selling products
- Product category performance
- Inventory levels
- Subscription plan distribution

### 3. SQL Analysis Using PostgreSQL

Imported the datasets into PostgreSQL and performed analytical SQL queries.

SQL concepts used include:

- SELECT, WHERE, GROUP BY, ORDER BY
- Aggregate functions
- INNER JOIN and other relational operations
- Common Table Expressions (CTEs)
- Window functions such as DENSE_RANK()
- Date-based analysis

Key SQL analyses include:

- Order status distribution
- Category-wise order value
- Top products by quantity
- Customer purchasing behavior
- Monthly delivered revenue
- Product ranking
- Low-stock inventory identification

### 4. Power BI Dashboard

Developed an interactive Power BI dashboard connected to PostgreSQL.

**Dashboard KPIs:**

| KPI | Value |
|---|---:|
| Total Orders | 1,000 |
| Delivered Orders | 503 |
| Delivered Revenue | 426,092.57 |
| Delivery Rate | 50.3% |

**Dashboard Visualizations:**

1. Total Orders KPI Card
2. Delivered Orders KPI Card
3. Delivered Revenue KPI Card
4. Order Status Distribution — Donut Chart
5. Monthly Delivered Revenue — Line Chart
6. Category-wise Order Value — Bar Chart
7. Top 10 Products by Ordered Quantity — Bar Chart
8. Category Slicer
9. Clear All Slicers Button

The dashboard allows users to interactively explore different product categories and analyze business performance.

## Dashboard Preview

[E-Commerce Sales Analysis Dashboard](Screenshots/powerbi_dashboard.png)

## Key Business Insights

### Order Performance

- Total orders analyzed: **1,000**
- Delivered orders: **503 (50.3%)**
- Cancelled orders: **144 (14.4%)**
- Returned orders: **123 (12.3%)**
- Processing orders: **118 (11.8%)**
- Shipped orders: **112 (11.2%)**

### Revenue Analysis

- Total recorded order value: **826,180.83**
- Delivered revenue: **426,092.57**

Delivered revenue is calculated using only orders with a delivered status. Total recorded order value includes orders of all statuses.

### Product Performance

- Identified the top 10 products based on ordered quantity.
- Analyzed category-wise product demand.
- Identified products with low inventory levels.

### Customer Analysis

- Analyzed customer purchasing frequency.
- Identified customers with the highest total order value.
- Explored subscription plan distribution.

## Business Recommendations

- Investigate cancellation and return patterns to improve order fulfillment.
- Prioritize inventory replenishment for frequently ordered, low-stock products.
- Monitor monthly delivered revenue to identify performance trends.
- Use customer purchase patterns to support retention and marketing strategies.
- Track category-level demand for better inventory planning.

## Project Structure

```text
E-commerce Analysis/
│
├── Data/
│   ├── customers-1000.csv
│   ├── orders-1000.csv
│   └── products-1000.csv
│
├── SQL/
│   └── ecommerce_analysis.sql
│
├── Screenshots/
│   └── powerbi_dashboard.png
│
├── Ecommerce_Dashboard.pbix
│
├── Python analysis files
│
└── README.md
```

## How to Run the Project

1. Clone or download the GitHub repository.
2. Install Python and the required analysis libraries.
3. Open the Python analysis files in VS Code.
4. Configure PostgreSQL and import the CSV datasets.
5. Execute the SQL queries from `SQL/ecommerce_analysis.sql`.
6. Open `Ecommerce_Dashboard.pbix` using Power BI Desktop.
7. Update the PostgreSQL data source connection if required.

## Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- SQL Querying and Database Management
- Data Aggregation and Joins
- Window Functions and CTEs
- Data Modeling
- DAX Measures
- Interactive Dashboard Development
- Business Insights and Reporting

## Conclusion

This project demonstrates an end-to-end data analytics workflow, from raw CSV datasets to SQL-based analysis and interactive Power BI reporting.

It highlights how Python, PostgreSQL, and Power BI can be integrated to analyze business performance and communicate actionable insights.
