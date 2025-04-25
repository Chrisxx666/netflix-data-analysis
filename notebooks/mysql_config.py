import os
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數
load_dotenv()

host = os.getenv("MYSQL_HOST", "localhost")
user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD", "")  # 預設為空密碼
database = os.getenv("MYSQL_DATABASE", "netflix_db")