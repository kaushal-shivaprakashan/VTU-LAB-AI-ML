import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('100.csv')

# Select the columns to use for the LOWESS plot
x =df['total_bill']
y = df['tip']
# Use the lowess function to compute the LOWESS fit
smooth = lowess(y, x,frac=0.05)

# Extract the x and y coordinates for the LOWESS line
smooth_x = smooth[:, 0]
smooth_y = smooth[:, 1]

# Plot the original data and the LOWESS line
plt.scatter(x, y,color='green')
plt.plot(smooth_x, smooth_y,color = 'red', linewidth=3)
plt.show()
