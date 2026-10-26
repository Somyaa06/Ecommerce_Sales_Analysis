CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    country VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE,
    plan VARCHAR(50),
    mrr NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    sku VARCHAR(50),
    order_date DATE,
    status VARCHAR(50),
    quantity INT,
    unit_price NUMERIC(10,2),
    subtotal NUMERIC(10,2),
    shipping NUMERIC(10,2),
    total NUMERIC(10,2)
);

CREATE TABLE products (
    sku VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    unit_cost NUMERIC(10,2),
    price NUMERIC(10,2),
    margin_pct NUMERIC(5,2),
    stock INT,
    rating NUMERIC(2,1),
    discontinued BOOLEAN
);

SELECT 'customers' AS table_name, COUNT(*) AS total_rows
FROM customers

UNION ALL

SELECT 'orders', COUNT(*)
FROM orders

UNION ALL

SELECT 'products', COUNT(*)
FROM products;


------ORDER STATUS ANALYSIS------

SELECT
    status,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS percentage
FROM orders
GROUP BY status
ORDER BY total_orders DESC;

-------CATEGORy - WISE SALES ANALYSIS-------

SELECT
    p.category,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(o.quantity) AS total_quantity,
    ROUND(SUM(o.total), 2) AS total_order_value
FROM orders o
JOIN products p
    ON o.sku = p.sku
GROUP BY p.category
ORDER BY total_order_value DESC;

----TOP 10 PRODUCTS by ORDER Quantity----
SELECT
    p.sku,
    p.product_name,
    p.category,
    SUM(o.quantity) AS total_quantity
FROM orders o
JOIN products p
    ON o.sku = p.sku
GROUP BY p.sku, p.product_name, p.category
ORDER BY total_quantity DESC
LIMIT 10;

-----CUSTOMER PURCHASE ANALYSIS------
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(
        SUM(CASE
            WHEN LOWER(o.status) = 'delivered'
            THEN o.total
            ELSE 0
        END), 0
    ) AS delivered_order_value
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY delivered_order_value DESC
LIMIT 10;

-----MONTHLY REVENUE ANALYSIS USING CTE----

WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date)::DATE AS month,
        COUNT(*) AS delivered_orders,
        SUM(total) AS revenue
    FROM orders
    WHERE LOWER(status) = 'delivered'
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT
    month,
    delivered_orders,
    ROUND(revenue, 2) AS monthly_revenue
FROM monthly_sales
ORDER BY month;

-----Rank Customers by Revenue Using Window Function-----

WITH customer_revenue AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        COALESCE(SUM(o.total), 0) AS revenue
    FROM customers c
    LEFT JOIN orders o
        ON c.customer_id = o.customer_id
        AND LOWER(o.status) = 'delivered'
    GROUP BY c.customer_id, c.first_name, c.last_name
)
SELECT
    customer_id,
    first_name,
    last_name,
    ROUND(revenue, 2) AS total_revenue,
    DENSE_RANK() OVER (
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM customer_revenue
ORDER BY revenue_rank
LIMIT 10;

-----LOW Stock Products Analysis-----

SELECT
    sku,
    product_name,
    category,
    stock
FROM products
WHERE stock <= 10
ORDER BY stock ASC;

