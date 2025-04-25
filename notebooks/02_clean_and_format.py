import pandas as pd
from utils import clean_dataframe  # 引入我們剛創建的函數

# 將清洗邏輯獨立出來，日後可以在其他檔案中重複使用，不需要複製貼上程式碼。

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

# 使用新的函數進行清洗
df = clean_dataframe(df)

df.to_csv('../data/netflix_cleaned.csv', index=False)
# Step5:optional - save cleaned dataset for future use 轉換日期格式

print("Data cleaned successfully!")
print(df.info())
# final check