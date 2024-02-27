import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read the data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6)

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot line of best fit
x_values = range(1880, 2051)
plt.plot(x_values, intercept + slope * x_values, color='red', label='Best Fit Line (1880-2050)')

# Linear regression from year 2000
recent_df = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
plt.plot(x_values, intercept_recent + slope_recent * x_values, color='blue', label='Best Fit Line (2000-2050)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and show plot
plt.savefig('sea_level_plot.png')
plt.show()
