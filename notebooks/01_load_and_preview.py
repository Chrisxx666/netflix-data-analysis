import pandas as pd
# import the pandas library for data handing

df = pd.read_csv('../data/netflix_titles.csv')
# load the dataset from the CSV file using a relative path

df.head()
# Show the first 5 rows (default). Use df.head(10) to view more.（quickly preview）

df.info()
# display general info about the dataset:num of rows, colum names, data type, non-null counts

df.isnull().sum()
# check how many missing values(nulls) exist in each colum

print(f'The dataset has {df.shape[0]} rows and {df.shape[1]} columns')