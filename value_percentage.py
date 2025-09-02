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
plt.xlabel('Initial Value')
plt.ylabel('Prime Density Percentage')
plt.grid(True)

plt.savefig(f"prime_density.pdf", bbox_inches="tight")
plt.savefig(f"prime_density.svg", bbox_inches="tight")

plt.tight_layout()
plt.show()
