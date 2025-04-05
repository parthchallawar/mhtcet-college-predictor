import pandas as pd

# Load the CSV file
input_csv_path = "rput.csv"  # Replace with the actual path to your CSV file
output_csv_path = "rputt.csv"  # Path to save the transformed CSV

# Read the CSV into a DataFrame
df = pd.read_csv(input_csv_path)

# Initialize an empty list to store the transformed data
transformed_data = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    college_id = row["Id"]
    college_name = row["College Name"]
    course = row["Course"]

    # Iterate over all seat types and their corresponding merit numbers and percentiles
    for seat_type in df.columns[3:]:  # Skip the first 3 columns (Id, College Name, Course)
        if "Percentile" in seat_type:
            continue
        merit_number = row[seat_type]
        percentile_column = f"{seat_type}_Percentile"  # Column name for percentile
        percentile = row.get(percentile_column, None)  # Get percentile if it exists

        # If merit_number is not NaN, add a new row to the transformed data
        if pd.notna(merit_number):
            transformed_data.append({
                "collegeid": college_id,
                "college name": college_name,
                "course": course,
                "merit number": merit_number,
                "seat type": seat_type,
                "percentile": percentile
            })

# Create a new DataFrame from the transformed data
transformed_df = pd.DataFrame(transformed_data)

# Save the transformed DataFrame to a new CSV file
transformed_df.to_csv(output_csv_path, index=False)

print(f"Transformed CSV saved to {output_csv_path}")
