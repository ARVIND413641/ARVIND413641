import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data and set index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5%
df_clean = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsiz
