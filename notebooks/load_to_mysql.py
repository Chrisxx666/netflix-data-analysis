import pandas as pd
import mysql.connector
from mysql_config import host, user, password, database

# 當處理大量資料時，批量插入比逐行插入效率高很多。處理 8000+ 資料列可以從幾分鐘縮短到幾秒鐘。

# 好處：
# 當程式發生錯誤時，日誌檔會記錄詳細情況，方便除錯
# 即使發生錯誤，也能確保資料庫連接正確關閉
# 可以追蹤程式執行的各個階段，了解每個步驟花費的時間

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

# 替換成這段程式碼
sql = """
    INSERT INTO netflix_titles 
    (show_id, type, title, director, `cast`, country, date_added, release_year, rating, duration, listed_in, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 分批處理，每次 1000 筆
batch_size = 1000
total_rows = len(df)

print(f"開始分批匯入資料，每批 {batch_size} 筆")
for i in range(0, total_rows, batch_size):
    # 取得目前批次的資料
    end_idx = min(i + batch_size, total_rows)
    batch = df.iloc[i:end_idx]

    # 準備批量插入的數據
    values = [tuple(row) for _, row in batch.iterrows()]

    # 批量插入
    cursor.executemany(sql, values)
    conn.commit()

    # 顯示進度
    progress = (end_idx / total_rows) * 100
    print(f"進度: {progress:.1f}% ({end_idx}/{total_rows})")

# 準備所有數據為元組列表
values = [tuple(row) for _, row in df.iterrows()]

# 批量插入 (一次性插入所有數據)
cursor.executemany(sql, values)

#5. Finalize and clean up
conn.commit()
cursor.close()
conn.close()

print("✅ Data has been successfully loaded into MySQL.")