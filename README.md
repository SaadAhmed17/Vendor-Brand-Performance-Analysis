**Vendor Sales Summary Data Analysis Project**
**Project Overview**

This project focuses on analyzing vendor sales and purchase performance data to uncover insights into profitability, vendor contribution, and brand performance. The goal is to support better business decision-making by identifying top-performing vendors/brands, low performers, profit margins, and unsold capital.

The analysis was carried out using Python, MySQL, and Power BI, combining data cleaning, transformation, visualization, and reporting into a structured workflow.

**Technologies & Tools Used**

🔹 Python (Pandas, NumPy, Matplotlib, Seaborn) – for data cleaning, transformation, and statistical analysis

🔹 MySQL – for data storage, querying, and vendor summary creation

🔹 SQLAlchemy / MySQL Connector – for database connections

🔹 Power BI – for building interactive dashboards

🔹 Logging & Error Handling – for tracking data ingestion and transformations

**Project Workflow**
**1. Data Ingestion & Cleaning**

🔹 Connected to MySQL database containing purchases, sales, prices, and vendor invoices.

🔹 Created a Vendor Sales Summary table using SQL queries (CTEs for freight, purchases, and sales).

🔹 Cleaned the data in Python:

🔹 Removed duplicates & nulls

🔹 Converted data types

🔹 Handled infinite values and missing values

🔹 Standardized vendor/brand names (removed trailing spaces)

**2. Feature Engineering**

🔹 New columns were created for deeper analysis:

🔹 Gross Profit = Total Sales Dollars – Total Purchase Dollars

🔹 Profit Margin = (Gross Profit ÷ Total Sales Dollars) × 100

🔹 Stock Turnover = Total Sales Quantity ÷ Total Purchase Quantity

🔹 Sales to Purchase Ratio = Total Sales ÷ Total Purchase

**3. Exploratory Data Analysis (EDA)**

🔹 Identified top vendors and brands contributing most to sales.

🔹 Detected low-performing vendors and brands with weak margins or low sales.

🔹 Analyzed inventory efficiency through unsold capital and stock turnover.

🔹 Applied confidence intervals & hypothesis testing to compare top vs. low-performing vendors.

**4. Visualization (Power BI Dashboard)**

🔹 Created an interactive dashboard to visualize:

🔹 Total Sales, Purchases, Gross Profit, Profit Margin, and Unsold Capital (KPI Cards)

🔹 Vendor contribution share (Donut Chart)

🔹 Top Vendors by Sales (Bar Chart)

🔹 Top Brands by Sales (Bar Chart)

🔹 Low Performing Vendors (Bar Chart)

🔹 Low Performing Brands (Scatter Plot with Profit Margin vs. Sales)

**Key Insights from Analysis**

🔹 Total Sales: $21.92M

🔹 Total Purchase: $15.52M

🔹 Gross Profit: $6.39M

🔹 Profit Margin: 47.46%

🔹 Unsold Capital: $1.29M tied up in inventory

🔹 Sales are heavily concentrated among a few vendors and brands, creating both risk and opportunity.
🔹 Several vendors and brands show low profit margins despite significant sales.
🔹 Unsold inventory is a concern, representing ~8% of purchases.

**Conclusion**
This project demonstrates how to integrate Python, SQL, and Power BI for end-to-end data analysis and visualization. It provides a practical framework for analyzing vendor performance, optimizing profitability, and improving supply chain decisions.
