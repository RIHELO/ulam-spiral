import pandas as pd
import matplotlib.pyplot as plt

# Read the file
df = pd.read_csv('data.csv', header=None, names=['Percentage', 'Value'], skipinitialspace=True)

# Normalize percentage values for color mapping
norm = plt.Normalize(df['Percentage'].min(), df['Percentage'].max())
cmap = plt.cm.Oranges

# Create scatter plot and store the mappable object
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['Value'], df['Percentage'], c=df['Percentage'], cmap=cmap, norm=norm, s=10)

# Labels and title
plt.xlabel('Value')
plt.ylabel('Percentage')
plt.title('Value vs Percentage (Color Intensity by Percentage)')
plt.grid(True)

# Add colorbar using the scatter object
plt.colorbar(scatter, label='Percentage')

plt.tight_layout()
plt.show()

