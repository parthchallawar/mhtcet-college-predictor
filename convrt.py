import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('put.csv')

# Define the columns to keep and unpivot
id_vars = ['Id', 'College Name', 'Course']
value_vars = [
    'DEFOBCS', 'DEFOPENS', 'DEFRNT1S', 'DEFRNT2S', 'DEFRNT3S', 'DEFROBCS', 'DEFRSCS', 'DEFRVJS', 'DEFSCS',
    'EWS', 'GNT1H', 'GNT1O', 'GNT1S', 'GNT2H', 'GNT2O', 'GNT2S', 'GNT3H', 'GNT3O', 'GNT3S',
    'GOBCH', 'GOBCO', 'GOBCS', 'GOPENH', 'GOPENO', 'GOPENS', 'GSCH', 'GSCO', 'GSCS', 'GSTH', 'GSTO', 'GSTS',
    'GVJH', 'GVJO', 'GVJS', 'LNT1H', 'LNT1O', 'LNT1S', 'LNT2H', 'LNT2O', 'LNT2S', 'LNT3H', 'LNT3O', 'LNT3S',
    'LOBCH', 'LOBCO', 'LOBCS', 'LOPENH', 'LOPENO', 'LOPENS', 'LSCH', 'LSCO', 'LSCS', 'LSTH', 'LSTO', 'LSTS',
    'LVJH', 'LVJO', 'LVJS', 'MI', 'ORPHAN', 'PWDOBCH', 'PWDOBCS', 'PWDOPENH', 'PWDOPENS', 'PWDRNT1S', 'PWDRNT2H',
    'PWDRNT2S', 'PWDROBC', 'PWDRSCH', 'PWDRSCS', 'PWDRVJH', 'PWDRVJS', 'PWDSCH', 'PWDSCS', 'TFWS'
]

# Unpivot the DataFrame
df_long = df.melt(id_vars=id_vars, value_vars=value_vars, var_name='Seat Type', value_name='Merit Number')

# Drop rows where Merit Number is NaN (empty)
df_long = df_long.dropna(subset=['Merit Number'])

# Rename columns to match the desired format
df_long = df_long.rename(columns={
    'Id': 'College ID',
    'College Name': 'Name',
    'Course': 'Branch'
})

# Save the transformed data to a new CSV
df_long.to_csv('transformed_data.csv', index=False)

print("Transformation complete! Check 'transformed_data.csv'.")
