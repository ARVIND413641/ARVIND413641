import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('medical_examination.csv')

# Add overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize cholesterol and glucose columns
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# Create a correlation matrix
corr = df.corr()

# Plot the correlation matrix
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', mask=mask, square=True, linewidths=0.5)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

# Convert the data into long format for visualization
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active'])

# Plot the categorical features using seaborn's catplot
sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
plt.show()
