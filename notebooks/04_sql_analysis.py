import pandas as pd
import plotly.express as px
from utils import connect_to_db  # 引入我們的新函數

# 優化後：避免在多個檔案中重複寫連接資料庫的程式碼，當資料庫設定改變時只需修改一處。

"""
This script connects to a MySQL database using SQLAlchemy,
retrieves Netflix data from the 'netflix_titles' table,
and generates visual insights including yearly trends,
content type distribution, ratings, and top countries.
"""

# Step 1: Connect to MySQL using our new function
engine = connect_to_db()

# Step 2: Read data from the MySQL table
df = pd.read_sql("SELECT * FROM netflix_titles", con=engine)

# Optional: Replace NaN with None for safety in downstream processing
df = df.where(pd.notnull(df), None)

# Extract the year from 'date_added'
df['year_added'] = pd.DatetimeIndex(df['date_added']).year

# -----------------------------
# Chart 1: Titles added per year
# -----------------------------
yearly_counts = df['year_added'].value_counts().sort_index()

fig = px.line(
    x=yearly_counts.index,
    y=yearly_counts.values,
    markers=True,
    labels={'x': 'Year', 'y': 'Number of Titles'},
    title='Number of Titles Added Each Year',
)
fig.show()

# -----------------------------
# Chart 2: Content type distribution (Movie vs TV Show)
# -----------------------------
type_counts = df['type'].value_counts()

fig = px.bar(
    x=type_counts.index,
    y=type_counts.values,
    labels={'x': 'Type', 'y': 'Count'},
    title='Distribution of Content Type on Netflix',
    text=type_counts.values
)
fig.update_traces(textposition='outside')
fig.update_layout(showlegend=False)
fig.show()

# -----------------------------
# Chart 3: Ratings distribution
# -----------------------------
rating_counts = df['rating'].value_counts().sort_values(ascending=False)

fig = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    labels={'x': 'Rating', 'y': 'Number of Titles'},
    title='Distribution of Content Ratings on Netflix',
    text=rating_counts.values
)
fig.update_traces(textposition='outside')
fig.update_layout(xaxis_tickangle=-45)
fig.show()

# -----------------------------
# Chart 4: Top 10 countries by number of titles
# -----------------------------
df['main_country'] = df['country'].apply(lambda x: x.split(',')[0].strip() if x else 'Unknown')
country_counts = df['main_country'].value_counts().head(10)

fig = px.bar(
    x=country_counts.values,
    y=country_counts.index,
    orientation='h',
    labels={'x': 'Num of Titles', 'y': 'Country'},
    title='Top 10 Countries by Number of Titles',
    text=country_counts.values,
)
fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Number of Titles',
    yaxis_title='Country',
    width=700,
    height=450,
    font=dict(size=14),
    plot_bgcolor='white',
    bargap=0.3
)
fig.show()
