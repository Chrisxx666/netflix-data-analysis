import pandas as pd

"""
這支程式是 Netflix 專案的第 2 階段，主要目的是對原始資料進行清洗與欄位格式轉換。

1. 檢查各欄位缺失值的狀況（isnull + sum）
2. 對 'director', 'cast', 'country', 'rating' 欄位補上預設值 'Unknown'
3. 移除 'title' 或 'date_added' 欄位為空的列（這些是關鍵資料）
4. 將 'date_added' 欄位轉換為 datetime 格式，方便後續做時間分析
5. 儲存一份清洗過後的新資料為 `netflix_cleaned.csv`

清洗資料是資料分析的第一個重要步驟，
能讓資料更乾淨、格式一致，也能避免後續分析時出現錯誤。
"""

df = pd.read_csv('../data/netflix_titles.csv')
# load the dataset to df

print(df.isnull().sum())
# Step1:check /w columns have missing value. Help us decide how to handle them
# 載入資料集

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
# Step2:fill missing values less critical columns 檢查缺失值
# prevents errors or bias in future analysis

df = df.dropna(subset=['title', 'date_added'])
# Step3:drop rows /w missing values in key columns 填補次要欄位缺失值
# We need title & date_added to be reliable

df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
# Step4:convert 'date_added' to datetime format 刪除關鍵欄位的缺失值
# useful for future time-based analysis

df.to_csv('../data/netflix_cleaned.csv', index=False)
# Step5:optional - save cleaned dataset for future use 轉換日期格式

print("Data cleaned successfully!")
print(df.info())
# final check