import pandas as pd

df = pd.read_csv('capacities.txt', sep='\t')

# Save the DataFrame to a CSV file
df.to_csv('capacities.csv', index=False)

print("The file 'capacities.txt' has been converted to 'capacities.csv'.")
