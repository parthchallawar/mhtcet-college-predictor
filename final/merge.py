import pandas as pd

college_details_df = pd.read_csv('./capacities.csv')

# Read the second CSV file containing CAP data
cap_data_df = pd.read_csv('./combined_cap_data.csv')

# Merge the two dataframes on the college name
merged_df = pd.merge(
    cap_data_df,
    college_details_df[['Institute Name', 'Status']],
    left_on='college name',
    right_on='Institute Name',
    how='left'
)

# Rename the 'Status' column to 'college type'
merged_df.rename(columns={'Status': 'college type'}, inplace=True)

# Drop the redundant 'Institute Name' column
merged_df.drop(columns=['Institute Name'], inplace=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_output.csv', index=False)

print("New CSV file 'merged_output.csv' has been created with the 'college type' column added.")
