# python_scripts/analytics.py
import pandas as pd
import mysql.connector

# Connect to the SQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="your_db"
)

query = "SELECT * FROM Tasks"
df = pd.read_sql(query, db)

# Perform analysis (e.g., task completion rates)
completion_rate = df['status'].value_counts(normalize=True) * 100
print(completion_rate)

db.close()
