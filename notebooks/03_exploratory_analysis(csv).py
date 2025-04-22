import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/netflix_cleaned.csv')

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
    title='Number of Titles Added Each Year'
)

fig.show()

# ========================== #
# Pic 2: Content Type Distribution
# ========================== #

"""
This chart compares the number of Movies and TV Shows available on Netflix.
Analyzing the 'type' column helps identify which format dominates.
"""

type_counts = df['type'].value_counts()

fig = px.bar(
    x=type_counts.index,
    y=type_counts.values,
    labels={'x': 'Type', 'y': 'Count'},
    title='Distribution of Content Type on Netflix',
    text=type_counts.values
)

fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Content Type',
    yaxis_title='Count',
    showlegend=False
)
fig.show()

# ========================== #
# Pic 3: Content Rating Distribution
# ========================== #

"""
This chart displays how Netflix content is distributed across different rating categories
(e.g., TV-MA, PG, R, etc.). It provides insight into the target audience.
"""

rating_counts = df['rating'].value_counts().sort_values(ascending=False)

fig = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    labels={'x': 'Rating', 'y': 'Number of Titles'},
    title='Distribution of Content Ratings on Netflix',
    text=rating_counts.values
)

fig.update_traces(textposition='outside')
fig.update_layout(
    xaxis_title='Rating',
    yaxis_title='Count',
    xaxis_tickangle=-45
)
fig.show()

# ========================== #
# Pic 4: Top 10 Countries by Number of Titles
# ========================== #

"""
This chart shows which countries have the most content on Netflix.
For rows with multiple countries, we only keep the first listed one.
"""

df['main_country'] = df['country'].apply(lambda x: x.split(',')[0].strip())
country_counts = df['main_country'].value_counts().head(10)

fig = px.bar(
    x=country_counts.values,
    y=country_counts.index,
    orientation='h',
    labels={'x': 'Number of Titles', 'y': 'Country'},
    title='Top 10 Countries by Number of Netflix Titles',
    text=country_counts.values
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
