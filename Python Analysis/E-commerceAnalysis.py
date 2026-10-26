import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load all the datasets

customers=pd.read_csv(r"F:\VISUAL STUDIO\PROJECTS\E-commerce Analysis\Data\customers-1000.csv")
orders=pd.read_csv(r"F:\VISUAL STUDIO\PROJECTS\E-commerce Analysis\Data\orders-1000.csv")
products=pd.read_csv(r"F:\VISUAL STUDIO\PROJECTS\E-commerce Analysis\Data\products-1000.csv")

print("All three datasets loaded successfully!")

# Check the dataset dimensions

print("Customers: ",customers.shape)
print("Orders: ",orders.shape)
print("Products: ",products.shape)

# Display the first five rows

print(customers.head())
print(orders.head())
print(products.head())

# Understanding the columns  and datatypes

print("CUSTOMERS INFO")
customers.info()
print("\n ORDERS INFO")
orders.info()
print("\nPRODUCTS INFO")
products.info()

# Checking Missing Values

print("Missing Values in Customers")
print(customers.isnull().sum())
print("\nMissing Values in Orders")
print(orders.isnull().sum())
print("\nMissing Values in Products")
print(products.isnull().sum())


print("\nDuplicate rows in Customers: ",customers.duplicated().sum())
print("Duplicate rows in Orders: ",orders.duplicated().sum())
print("Duplicate rows in Products: ",products.duplicated().sum())


# Check whether the important IDs are unique

print("\n--- DUPLICATE IDs ---")
print("Customer IDs:", customers["customer_id"].duplicated().sum())
print("Order IDs:", orders["order_id"].duplicated().sum())
print("Product SKUs:", products["sku"].duplicated().sum())


# Converting the date Columns

customers["signup_date"]=pd.to_datetime(
    customers["signup_date"],
    format="%d-%m-%Y",
    errors="coerce"
)   # errors= coerce converts invalid dates into Nat(missing datetime values)

orders["order_date"]=pd.to_datetime(
    orders["order_date"],
    format="%d-%m-%Y",errors='coerce'
)

# Check for invalid or missing dates   - Data Cleaning'
print("\n--- DATE VALIDATION ---")

print(
    "Invalid or missing signup dates:",
    customers["signup_date"].isna().sum()
)

print(
    "Invalid or missing order dates:",
    orders["order_date"].isna().sum()
)

# Check relationship between datasets
# check whether each order's customer exists
missing_customers=orders[~orders["customer_id"].isin(customers["customer_id"])]
missing_products=orders[~orders["sku"].isin(products["sku"])]
# .isin check id ID is present in other dataswr
# ~ means NOT
# len() counts unmatching failure
print("\n------RELATIONSHIP VALIDATION------")
print("Orders with missing customers: ",len(missing_customers))
print("Orders with missing products: ",len(missing_products ))

# Basic sales Analysis
# Total number of orders
total_orders= orders["order_id"].nunique()
# Total revenue
total_revenue = orders["total"].sum()
# Average order value
average_order_value = orders["total"].mean()
# Total quanntity of products ordered
total_quantity = orders["quantity"].sum()

print("]n----BASIC SALES ANALYSIS-----")
print("Total Orders: ",total_orders)  #total order placed
print("Total Revenue: ",round(total_revenue,2)) # total column values sum
print("Average Order Value: ",round(average_order_value,2)) #average total amount of every order
print("Total Quantity Sold: ",total_quantity) #summ of product quantities listed in orders

# Order Status Analysis
# Count orders  by status

status_counts=orders["status"].value_counts() 
print("\n----ORDER STATUS ANALYSIS----")
print(status_counts)

#Calculate percentage of each status
status_percentage=(orders["status"].value_counts(normalize=True)*100) #finds proportion of every status. *100 converts proportio to percentage
print("\n----ORDER STATUS PERCENTAGE----")
print(status_percentage.round(2))

# Revenue Analysis

# Total recorded order value
total_revenue = orders["total"].sum()

# Revenue by order status
revenue_by_status = orders.groupby("status")["total"].sum()

print("\n----TOTAL RECORDED REVENUE----")
print(round(total_revenue,2))
print("\n----REVENUE BY ORDER STATUS----")
print(revenue_by_status.round(2))

# Revenue from delivered orders only
delivered_revenue = orders.loc[orders["status"]=="delivered","total"].sum()
print("\n----DELIVERED ORDER VALUE----")
print(round(delivered_revenue,2))

# Customer Analysis

# Total unique ustomers
total_customers = customers["customer_id"].nunique()

#Number of orders placed by each customer
orders_per_customer = orders.groupby("customer_id")["order_id"].nunique()

# Top 10 customers by number of orders
top_customers = orders_per_customer.sort_values(ascending=False).head(10)
print("\n----CUSTOMER ANALYSIS----")
print("Total Unique Customers: ",total_customers)

print("\n----TOP 10 CUSTOMERS BY ORDER COUNT---- ")
print(top_customers)


# Customer Revenue Analysis

#Calculate total order value for each customer
customer_revenue=orders.groupby("customer_id")["total"].sum()
# Sort customers by highest order value
top_revenue_customers = customer_revenue.sort_values(ascending=False).head(10)
print("\n---TOP 10 CUSTOMERS BY RECORDED ORDER VALUE---")
print(top_revenue_customers.round(2))



#  Product Analysis

# Calculate total quantity sold for each product
product_sales = orders.groupby("sku")["quantity"].sum()

# Sort products from highest to lowest quantity
top_products = product_sales.sort_values(
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY QUANTITY SOLD ---")
print(top_products)


# Top products with Product Names

# Calculate total quantity sold for each SKU
product_sales=orders.groupby("sku")["quantity"].sum()

# Convert the result into a DataFrame
product_sales=product_sales.reset_index()

# Add product names using the products dataset
product_sales = product_sales.merge(
    products[["sku","product_name","category"]],
    on="sku",how="left"
)

# Show the top 10mproducts
top_products= product_sales.sort_values(
    by="quantity",ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS WITH NAMES ---")
print(top_products[["sku", "product_name", "category", "quantity"]].to_string(index=False))


# Category-wise Sales Analysis

# Combine orders with product cateegories
orders_with_products = orders.merge(
    products[["sku", "product_name", "category"]],
    on="sku",
    how="left"
)

# Calculate total quantity for each category
category_sales= orders_with_products.groupby("category")["quantity"].sum()

# Sort categgories  from highest to Lowest quantity
category_sales= category_sales.sort_values(ascending=False)

print("\n----CATEGORY WISE QUANTITY SOLD----")
print(category_sales )


# Visualize category-wise sales using a bar chart

# categgory wise Sales Bar Chart
category_sales.plot(kind="bar",figsize=(8,5))

plt.title("Category-wise Quantity Sold")
plt.xlabel("Product Categgory")
plt.ylabel("Total Quantity") 
plt.xticks(rotation=0)  #Controls x axis tick labels
plt.tight_layout()
plt.show()  


# Monthlly Sales Analysis

# Extract month from order date
orders["order_month"]=orders["order_date"].dt.to_period("M")

# Calculate Monthly recorded order  value
monthly_sales= orders.groupby("order_month")["total"].sum()

print("\n---MONTHLY RECORDED ORDER VALUE---")
print(monthly_sales.round(2))

#Plot monthly sales
monthly_sales.plot(kind="line",marker="o",figsize=(10,5))

plt.title("Monthly Recorded Order Value")
plt.xlabel("Month")
plt.ylabel("Recorded Order Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Order Status wise Revenue Analysis
revenue_by_status= orders.groupby("status")["total"].sum()

# Sort from higest to lowest
revenue_by_status=revenue_by_status.sort_values(ascending=False)

print("\n------RECORDED ORDER VALUE BY STATUS----")
print(revenue_by_status.round(2))

# Create a bar chart
revenue_by_status.plot(kind="bar", figsize=(8,5))

plt.title("Recordded Order Value by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Recorded Order Value")
plt.xticks(rotation=45)  # prevents overlaps
plt.tight_layout()
plt.show()

# Order Status Percentage Analysis

status_percentage= orders["status"].value_counts(normalize=True)*100
status_percentage= status_percentage.round(2)

print("\n----ORDER STATUS PERCENTAGE----")
print(status_percentage)

# Create a pie chart
status_percentage.plot(kind="pie",autopct="%1.1f%%",figsize=(7,7))

plt.title("Order Status Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Product Profit Analysis

# Calculate profit per unit
products["profit_per_unit"]=products["price"]-products["unit_cost"]

# Calculate total recorded quantity for each product
product_sales= orders.groupby("sku")["quantity"].sum().reset_index()

#Add product details
product_profit=product_sales.merge(
    products[["sku","product_name","category","unit_cost","price","profit_per_unit"]],
    on="sku",
    how="left"
)
# Estimate total profit
product_profit["estimated_profit"] = (
    product_profit["quantity"] * product_profit["profit_per_unit"]
)

# Show top 10 products by estimated profit
top_profit_products = product_profit.sort_values(
    by="estimated_profit",
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY ESTIMATED PROFIT ---")
print(
    top_profit_products[
        ["product_name", "category", "quantity", "profit_per_unit",
         "estimated_profit"]
    ].round(2).to_string(index=False)
)

# Top 10 Products by Estimated Profit Chart

top_profit_products.plot(
    x="product_name",
    y="estimated_profit",
    kind="bar",
    figsize=(12,6),
    legend=False
)
plt.title("Top 10 Products by Estimated Profit")
plt.xlabel("Product Name")
plt.ylabel("Estimated Profit")
plt.xticks(rotation=45,ha="right") # ha="right" it right aligned rotated labels to improve readability.
plt.tight_layout()
plt.show()

#  Category-wise Estimated Profit

category_profit = product_profit.groupby("category")["estimated_profit"].sum()

category_profit = category_profit.sort_values(ascending=False)

print("\n--- CATEGORY-WISE ESTIMATED PROFIT ---")
print(category_profit.round(2))

category_profit.plot(kind="bar", figsize=(8, 5))

plt.title("Category-wise Estimated Profit")
plt.xlabel("Product Category")
plt.ylabel("Estimated Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#  Monthly Order Count Analysis

orders["order_month"] = orders["order_date"].dt.to_period("M")

monthly_orders = orders.groupby("order_month")["order_id"].nunique()

print("\n--- MONTHLY ORDER COUNT ---")
print(monthly_orders)

monthly_orders.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Monthly Order Count")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Monthly Revenue Trend

monthly_revenue = orders.groupby("order_month")["total"].sum()

print("\n--- MONTHLY RECORDED ORDER VALUE ---")
print(monthly_revenue.round(2))

monthly_revenue.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)

plt.title("Monthly Recorded Order Value Trend")
plt.xlabel("Month")
plt.ylabel("Recorded Order Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Customer Plan Analysis

plan_analysis = customers.groupby("plan").agg(
    total_customers=("customer_id", "nunique"),
    total_mrr=("mrr", "sum"),  # mrr- Monthly Recurring Revenue
    average_mrr=("mrr", "mean")
)

plan_analysis = plan_analysis.sort_values(
    by="total_mrr",
    ascending=False
)

print("\n--- CUSTOMER PLAN ANALYSIS ---")
print(plan_analysis.round(2))

# Category wise Recorded Order Value

orders_with_products= orders.merge(
    products[["sku","category"]],
    on="sku",
    how="left"
)

category_revenue= orders_with_products.groupby("category")["total"].sum()
category_revenue=category_revenue.sort_values(ascending=False)
print("\n----CATEGORY-WISE RECORDED ORDER VALUE----")
print(category_revenue.round(2))

category_revenue.plot(kind="bar",figsize=(8,5))
plt.title("Category-wise Recorded Order Value")
plt.xlabel("Product Category")
plt.ylabel("Recorded Order Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Low-Stock Product Analysis

low_stock_products = products[
    products["stock"] <= 10
].sort_values(by="stock")

print("\n--- LOW-STOCK PRODUCTS ---")

print(
    low_stock_products[
        ["sku", "product_name", "category", "stock"]
    ].to_string(index=False)
)

print("\nTotal low-stock products:", len(low_stock_products))


# Top-Rated Products

top_rated_products=products[products["rating"].notna()].sort_values(
    by="rating",
    ascending=False
).head(10)

print("\n----TOP 10 RATED PRODUCTS----")
print(
    top_rated_products[["sku","product_name","category","rating"]].to_string(index=False)
)


# Final Business Insights

print("\n======================E-COMMERCE BUSINESS INSIGHTS=========================")
print("Total uniques orders: ",orders["order_id"].nunique())
print("Total customers: ",customers["customer_id"].nunique())

print("\nMost common order status: ")
print(orders["status"].value_counts().idxmax())

print("\nCategory with highest recorded order value: ")
print(category_revenue.idxmax(),
      round(category_revenue.max(),2))

print("\nCategory with lowest recorded order value: ")
print(category_revenue.idxmin(),
      round(category_revenue.min(),2))

print("\nHighest MRR customer plan: ")
print(plan_analysis["total_mrr"].idxmax(),
      round(plan_analysis["total_mrr"].max(),2))

print("\nNumber of low-stock products: ",
      len(low_stock_products))

print("\nHighest product rating: ",
      products["rating"].max())

print("\n===========================================")