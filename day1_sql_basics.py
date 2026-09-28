import sqlite3

# ============================================================
# PART 1 - CONNECT TO DATABASE
# ============================================================

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

print("=" * 60)
print("SQL BASICS - STORE DATABASE")
print("=" * 60)

print("\nConnection successful!")


# ============================================================
# PART 2 - CREATE TABLES AND INSERT DATA
# ============================================================

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
)
""")

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    sale_date TEXT,
    city TEXT
)
""")

# ------------------------------------------------------------
# Insert 10 products
# ------------------------------------------------------------

products = [
    (1, "Laptop", "electronics", 800),
    (2, "Mouse", "electronics", 25),
    (3, "Keyboard", "electronics", 50),
    (4, "Monitor", "electronics", 250),
    (5, "Headphones", "electronics", 75),
    (6, "Webcam", "electronics", 100),
    (7, "Printer", "electronics", 300),
    (8, "USB Cable", "electronics", 15),
    (9, "Tablet", "electronics", 450),
    (10, "Charger", "electronics", 30)
]

cursor.executemany("""
INSERT OR IGNORE INTO products
(product_id, product_name, category, price)
VALUES (?, ?, ?, ?)
""", products)

# ------------------------------------------------------------
# Insert 30 sales
# ------------------------------------------------------------

sales = [
    (1, 1, 3, "2026-01-05", "Amman"),
    (2, 2, 10, "2026-01-06", "Amman"),
    (3, 3, 6, "2026-01-07", "Zarqa"),
    (4, 4, 4, "2026-01-08", "Irbid"),
    (5, 5, 8, "2026-01-09", "Amman"),
    (6, 6, 5, "2026-01-10", "Zarqa"),
    (7, 7, 2, "2026-01-11", "Irbid"),
    (8, 8, 15, "2026-01-12", "Amman"),
    (9, 9, 4, "2026-01-13", "Aqaba"),
    (10, 10, 12, "2026-01-14", "Zarqa"),
    (11, 1, 2, "2026-01-15", "Irbid"),
    (12, 2, 8, "2026-01-16", "Aqaba"),
    (13, 3, 5, "2026-01-17", "Amman"),
    (14, 4, 3, "2026-01-18", "Zarqa"),
    (15, 5, 7, "2026-01-19", "Irbid"),
    (16, 6, 6, "2026-01-20", "Amman"),
    (17, 7, 3, "2026-01-21", "Aqaba"),
    (18, 8, 20, "2026-01-22", "Zarqa"),
    (19, 9, 5, "2026-01-23", "Amman"),
    (20, 10, 10, "2026-01-24", "Irbid"),
    (21, 1, 4, "2026-01-25", "Aqaba"),
    (22, 2, 12, "2026-01-26", "Zarqa"),
    (23, 3, 7, "2026-01-27", "Amman"),
    (24, 4, 5, "2026-01-28", "Irbid"),
    (25, 5, 9, "2026-01-29", "Aqaba"),
    (26, 6, 4, "2026-01-30", "Zarqa"),
    (27, 7, 2, "2026-01-31", "Amman"),
    (28, 8, 18, "2026-02-01", "Irbid"),
    (29, 9, 6, "2026-02-02", "Zarqa"),
    (30, 10, 14, "2026-02-03", "Amman")
]

cursor.executemany("""
INSERT OR IGNORE INTO sales
(sale_id, product_id, quantity, sale_date, city)
VALUES (?, ?, ?, ?, ?)
""", sales)

conn.commit()

print("\nTables and data created successfully.")


# ============================================================
# PART 3 - SELECT, WHERE, ORDER BY
# ============================================================

print("\n" + "=" * 60)
print("PART 3 - SELECT, WHERE, ORDER BY")
print("=" * 60)

# 1. All products
print("\n1. All Products:")

cursor.execute("""
SELECT * FROM products
""")

for row in cursor.fetchall():
    print(row)


# 2. Products with price greater than 50
print("\n2. Products with Price > 50:")

cursor.execute("""
SELECT product_name, price
FROM products
WHERE price > 50
""")

for row in cursor.fetchall():
    print(row)


# 3. Sales in Amman ordered by date
print("\n3. Sales in Amman:")

cursor.execute("""
SELECT *
FROM sales
WHERE city = 'Amman'
ORDER BY sale_date ASC
""")

for row in cursor.fetchall():
    print(row)


# 4. Electronics under 100
print("\n4. Electronics with Price < 100:")

cursor.execute("""
SELECT product_name, category, price
FROM products
WHERE category = 'electronics'
AND price < 100
""")

for row in cursor.fetchall():
    print(row)


# 5. Top 5 sales by quantity
print("\n5. Top 5 Sales by Quantity:")

cursor.execute("""
SELECT *
FROM sales
ORDER BY quantity DESC
LIMIT 5
""")

for row in cursor.fetchall():
    print(row)


# ============================================================
# PART 4 - GROUP BY AND AGGREGATION
# ============================================================

print("\n" + "=" * 60)
print("PART 4 - GROUP BY AND AGGREGATION")
print("=" * 60)

# 1. Total quantity sold per product
print("\n1. Total Quantity Sold per Product:")

cursor.execute("""
SELECT product_id, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_id
ORDER BY total_quantity DESC
""")

for row in cursor.fetchall():
    print(row)


# 2. Number of sales per city
print("\n2. Number of Sales per City:")

cursor.execute("""
SELECT city, COUNT(*) AS number_of_sales
FROM sales
GROUP BY city
ORDER BY number_of_sales DESC
""")

for row in cursor.fetchall():
    print(row)


# 3. Average product price per category
print("\n3. Average Price per Category:")

cursor.execute("""
SELECT category, AVG(price) AS average_price
FROM products
GROUP BY category
""")

for row in cursor.fetchall():
    print(row)


# 4. City with the largest number of sales
print("\n4. City with the Largest Number of Sales:")

cursor.execute("""
SELECT city, COUNT(*) AS number_of_sales
FROM sales
GROUP BY city
ORDER BY number_of_sales DESC
LIMIT 1
""")

print(cursor.fetchone())


# ============================================================
# PART 5 - BUSINESS QUESTIONS
# ============================================================

print("\n" + "=" * 60)
print("PART 5 - BUSINESS QUESTIONS")
print("=" * 60)


# 1. Top 3 best-selling products by total quantity
print("\n1. Top 3 Best-Selling Products:")

cursor.execute("""
SELECT
    p.product_name,
    SUM(s.quantity) AS total_quantity
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 3
""")

for row in cursor.fetchall():
    print(row)


# 2. Total revenue per product
print("\n2. Total Revenue per Product:")

cursor.execute("""
SELECT
    p.product_name,
    SUM(s.quantity * p.price) AS total_revenue
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
""")

for row in cursor.fetchall():
    print(row)


# 3. City with highest total quantity sold
print("\n3. City with Highest Total Quantity Sold:")

cursor.execute("""
SELECT
    city,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY city
ORDER BY total_quantity DESC
LIMIT 1
""")

print(cursor.fetchone())


# 4. Category with the most sales transactions
print("\n4. Category with the Most Sales Transactions:")

cursor.execute("""
SELECT
    p.category,
    COUNT(*) AS number_of_sales
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY number_of_sales DESC
LIMIT 1
""")

print(cursor.fetchone())


# 5. Average quantity per sale
print("\n5. Average Quantity per Sale:")

cursor.execute("""
SELECT AVG(quantity)
FROM sales
""")

print(cursor.fetchone())


# ============================================================
# BUSINESS SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("BUSINESS SUMMARY")
print("=" * 60)

print("""
The analysis shows which products generate the highest sales volume
and revenue. It also identifies the city with the highest total
quantity sold and shows the sales distribution across product
categories. These results can help the store understand customer
demand and make better inventory and sales decisions.
""")


# ============================================================
# FINAL CHECK
# ============================================================

cursor.execute("SELECT COUNT(*) FROM products")
product_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM sales")
sales_count = cursor.fetchone()[0]

print("Total products:", product_count)
print("Total sales:", sales_count)

conn.close()

print("\nDatabase connection closed successfully.")