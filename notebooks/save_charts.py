import os
import pandas as pd
import plotly.express as px
import plotly.io as pio

"""
這個腳本用於生成分析圖表並將其保存為圖片，
這些圖片可以用於網站展示和分享。
"""

# 確保輸出目錄存在
output_dir = "../website/images"
os.makedirs(output_dir, exist_ok=True)

# 載入清洗後的資料
df = pd.read_csv('../data/netflix_cleaned.csv')

# 設置統一的圖表主題和顏色
template = "plotly_white"
colors = {
    'primary': '#E50914',    # Netflix 紅
    'secondary': '#221F1F',  # Netflix 黑
    'background': '#F5F5F1'  # 淺灰色背景
}

# ========================== #
# 圖表 1: 每年內容增長趨勢
# ========================== #
df['year_added'] = pd.DatetimeIndex(df['date_added']).year
yearly_counts = df['year_added'].value_counts().sort_index()

fig1 = px.line(
    x=yearly_counts.index,
    y=yearly_counts.values,
    markers=True,
    labels={'x': 'Year', 'y': 'Number of Titles'},
    title='Netflix Content Growth by Year',
    template=template
)

fig1.update_traces(
    line=dict(color=colors['primary'], width=3),
    marker=dict(size=8, color=colors['primary'])
)
fig1.update_layout(
    plot_bgcolor=colors['background'],
    font=dict(family="Arial, sans-serif", size=14),
    title_font_size=20,
    hoverlabel=dict(bgcolor="white", font_size=14)
)

# 保存圖表 1
pio.write_image(fig1, f"{output_dir}/yearly_growth.png", scale=2, width=1000, height=600)
print(f"已保存: yearly_growth.png")

# ========================== #
# 圖表 2: 內容類型分佈
# ========================== #
type_counts = df['type'].value_counts()

fig2 = px.bar(
    x=type_counts.index,
    y=type_counts.values,
    labels={'x': 'Type', 'y': 'Count'},
    title='Content Type Distribution',
    template=template,
    text=type_counts.values,
    color=type_counts.index,
    color_discrete_map={'Movie': colors['primary'], 'TV Show': colors['secondary']}
)

fig2.update_traces(textposition='outside')
fig2.update_layout(
    plot_bgcolor=colors['background'],
    font=dict(family="Arial, sans-serif", size=14),
    title_font_size=20,
    hoverlabel=dict(bgcolor="white", font_size=14),
    showlegend=False
)

# 保存圖表 2
pio.write_image(fig2, f"{output_dir}/content_types.png", scale=2, width=1000, height=600)
print(f"已保存: content_types.png")

# ========================== #
# 圖表 3: 評分分佈
# ========================== #
rating_counts = df['rating'].value_counts().sort_values(ascending=False).head(10)

fig3 = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    labels={'x': 'Rating', 'y': 'Number of Titles'},
    title='Top 10 Content Ratings on Netflix',
    template=template,
    text=rating_counts.values,
    color_discrete_sequence=[colors['primary']] * len(rating_counts)
)

fig3.update_traces(textposition='outside')
fig3.update_layout(
    plot_bgcolor=colors['background'],
    font=dict(family="Arial, sans-serif", size=14),
    title_font_size=20,
    hoverlabel=dict(bgcolor="white", font_size=14),
    xaxis_tickangle=-45
)

# 保存圖表 3
pio.write_image(fig3, f"{output_dir}/rating_distribution.png", scale=2, width=1000, height=600)
print(f"已保存: rating_distribution.png")

# ========================== #
# 圖表 4: 主要國家
# ========================== #
df['main_country'] = df['country'].apply(lambda x: x.split(',')[0].strip() if x else 'Unknown')
country_counts = df['main_country'].value_counts().head(10)

fig4 = px.bar(
    x=country_counts.values,
    y=country_counts.index,
    orientation='h',
    labels={'x': 'Number of Titles', 'y': 'Country'},
    title='Top 10 Countries by Number of Netflix Titles',
    template=template,
    text=country_counts.values,
    color_discrete_sequence=[colors['primary']] * len(country_counts)
)

fig4.update_traces(textposition='outside')
fig4.update_layout(
    plot_bgcolor=colors['background'],
    font=dict(family="Arial, sans-serif", size=14),
    title_font_size=20,
    hoverlabel=dict(bgcolor="white", font_size=14),
    height=600
)

# 保存圖表 4
pio.write_image(fig4, f"{output_dir}/top_countries.png", scale=2, width=1000, height=600)
print(f"已保存: top_countries.png")

print("\n✅ 所有圖表已成功生成並保存！")