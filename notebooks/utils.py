# notebooks/utils.py
import pandas as pd


def clean_dataframe(df):
    """執行基本的數據清洗操作"""
    # 建立 DataFrame 的拷貝以避免警告
    df = df.copy()

    # 填充缺失值
    df.loc[:, 'director'] = df['director'].fillna('Unknown')
    df.loc[:, 'cast'] = df['cast'].fillna('Unknown')
    df.loc[:, 'country'] = df['country'].fillna('Unknown')
    df.loc[:, 'rating'] = df['rating'].fillna('Unknown')

    # 刪除關鍵欄位缺失的行
    df = df.dropna(subset=['title', 'date_added'])

    # 日期格式轉換
    df.loc[:, 'date_added'] = pd.to_datetime(df['date_added'].str.strip())

    return df


# 在 notebooks/utils.py 中添加以下函數

def connect_to_db():
    """建立資料庫連接並返回連接物件"""
    from sqlalchemy import create_engine
    from mysql_config import host, user, password, database

    connection_string = f"mysql+pymysql://{user}:{password}@{host}/{database}?unix_socket=/tmp/mysql.sock"
    return create_engine(connection_string)