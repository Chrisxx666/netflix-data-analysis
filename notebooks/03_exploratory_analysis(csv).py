import pandas as pd
import plotly.express as px

# 載入資料
df = pd.read_csv('../data/netflix_cleaned.csv')

# 設置統一的圖表主題和顏色
template = "plotly_white"
colors = {
    'primary': '#E50914',    # Netflix 紅
    'secondary': '#221F1F',  # Netflix 黑
    'background': '#F5F5F1'  # 淺灰色背景
}

# ========================== #
# Pic 1: Yearly Content Growth
# ========================== #

"""
This chart shows how many titles were added to Netflix each year.
It helps us observe content growth trends over time.
"""

df['year_added'] = pd.DatetimeIndex(df['date_added']).year
yearly_counts = df['year_added'].value_counts().sort_index()

fig = px.line(
    x=yearly_counts.index,
    y=yearly_counts.values,
    markers=True,
    labels={'x': 'Year', 'y': 'Number of Titles'},
    title='Netflix 每年新增內容數量',
    template=template
)

# 【優化】美化圖表
fig.update_traces(
    line=dict(color=colors['primary'], width=3),
    marker=dict(size=8, color=colors['primary'])
)
fig.update_layout(
    plot_bgcolor=colors['background'],
    font=dict(family="Arial, sans-serif", size=14),
    title_font_size=20,
    hoverlabel=dict(bgcolor="white", font_size=14)
)

fig.show()

# ========================== #
# Pic 2: Content Type Distribution
# ========================== #

# 其他圖表代碼也做類似修改...