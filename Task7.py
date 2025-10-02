import sqlite3

# Define the database file name
DB_FILE = "sales_data.db"

# 1. Connect to the database (it will create the file if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# 2. Drop the table if it exists to ensure a clean start
cursor.execute("DROP TABLE IF EXISTS sales;")

# 3. Create the 'sales' table
create_table_query = """
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
);
"""
cursor.execute(create_table_query)

# 4. Insert sample sales data
sales_data = [
    ('Laptop', 5, 1200.00),
    ('Monitor', 10, 300.50),
    ('Laptop', 3, 1200.00),
    ('Keyboard', 25, 75.00),
    ('Monitor', 8, 300.50),
    ('Mouse', 40, 25.99)
]

insert_query = "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?);"
cursor.executemany(insert_query, sales_data)

# 5. Commit changes and close the connection
conn.commit()
conn.close()

print(f"Database '{DB_FILE}' created and populated with 6 sales records.")

# Another file

# 1. Import necessary libraries
import sqlite3 # To connect to the database [cite: 8, 18]
import pandas as pd # To run the query and handle data [cite: 8, 22]
import matplotlib.pyplot as plt # To create the chart [cite: 8]

# 2. Define the database file name
DB_FILE = "sales_data.db"

# 3. Connect to the SQLite database
# The connection object 'conn' is created[cite: 18].
conn = sqlite3.connect(DB_FILE)

# 4. Define the SQL query
# This query aggregates data:
# - SUM(quantity) gives the total units sold.
# - SUM(quantity * price) calculates the total revenue for all records in the group.
# - GROUP BY product summarizes the results for each unique product[cite: 20, 21].
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM 
    sales 
GROUP BY 
    product
ORDER BY
    revenue DESC;
"""

# 5. Load the SQL query results into a pandas DataFrame
# pd.read_sql_query executes the query and returns a DataFrame[cite: 22].
df = pd.read_sql_query(query, conn)

# 6. Close the database connection
conn.close()

# 7. Print the results (Deliverable)
print("--- Basic Sales Summary by Product ---")
print(df) # [cite: 23]

# 8. Plot a simple bar chart (Deliverable)
# Plotting the 'revenue' against the 'product'[cite: 24].
df.plot(
    kind='bar',
    x='product',
    y='revenue',
    title='Total Revenue by Product',
    legend=False,
    color='skyblue'
)
plt.ylabel('Total Revenue ($)')
plt.xlabel('Product')
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.grid(axis='y', linestyle='--')
plt.tight_layout() # Adjust layout to prevent labels from being cut off

# 9. Save and display the chart
plt.savefig("sales_chart.png") # [cite: 25]
print("\nChart saved as 'sales_chart.png'")

plt.show()
