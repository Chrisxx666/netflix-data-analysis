import pandas as pd
import mysql.connector
from mysql_config import host, user, password, database

"""
This script reads the cleaned Netflix dataset from CSV
and writes it into the MYSQL table 'netflix_titles'
"""

#1. Load CSV as a pandas DataFrame
csv_path = "../data/netflix_cleaned.csv"
df = pd.read_csv(csv_path)

# (*)補這一行，將 NaN 轉成 None
df = df.where(pd.notnull(df), None)

#2. Connect to the MySQL database using the config
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    unix_socket="/tmp/mysql.sock"  # 或你查到的那條 socket 路徑
)

cursor = conn.cursor()

#3. Optional: Clear the table first to avoid duplication
cursor.execute("DELETE FROM netflix_titles")
conn.commit()

#4. Insert each row from the DataFrame into the database
for _, row in df.iterrows():
    sql = """
        INSERT INTO netflix_titles 
        (show_id, type, title, director, `cast`, country, date_added, release_year, rating, duration, listed_in, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = tuple(row)
    cursor.execute(sql, values)

#5. Finalize and clean up
conn.commit()
cursor.close()
conn.close()

print("✅ Data has been successfully loaded into MySQL.")
