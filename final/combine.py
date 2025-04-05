import os
import pandas as pd

folder_path = '.'

output_file = 'combined_cap_data.csv'

dataframes = []

for file in os.listdir(folder_path):
    if file.endswith('.csv') and 'CAP' in file:
        # Extract Academic Year and Cap Round from the filename
        parts = file.split('_')
        academic_year = parts[0]
        cap_round = parts[1].replace('.csv', '')

        # Read the CSV file
        df = pd.read_csv(os.path.join(folder_path, file))

        # Add new columns
        df['Academic Year'] = academic_year
        df['Cap Round'] = cap_round

        # Append to the list
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

combined_df.to_csv(output_file, index=False)

print(f'Combined data saved to {output_file}')
