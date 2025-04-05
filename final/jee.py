import csv
import re

# Input and output file paths
input_txt_path = "./extracted_text.txt"  # Replace with the actual path to your text file
output_csv_path = "output.csv"  # Path to save the CSV file

# Function to extract data from the text file
def extract_data(lines):
    data = []
    for line in lines:
        # Use a simpler regex pattern to capture the required fields
        match = re.match(
            r"(\d+,\d+)\s+(\d+)\s+\(([\d.]+)\)\s+(\d+)\s+(.+)",
            line.strip(),
        )
        if match:
            sr_no = match.group(1).replace(",", "")  # Remove commas from Sr. No
            merit_number = match.group(2)
            percentile = match.group(3)
            college_name = match.group(5).strip()
            # Append the data to the list
            data.append([sr_no, merit_number, percentile, college_name])
        else:
            # Debugging: Print lines that don't match the pattern
            print(f"Skipping line (no match): {line.strip()}")
    return data

# Read the text file
with open(input_txt_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract data
data = extract_data(lines)

# Write to CSV
with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # Write header
    writer.writerow(["Sr. No", "Merit Number", "Percentile", "College Name"])
    # Write rows
    writer.writerows(data)

print(f"CSV file saved to {output_csv_path}")
