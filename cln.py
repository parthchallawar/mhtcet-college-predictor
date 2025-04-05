import csv
from collections import defaultdict

# Input and Output file paths
csv_input_path = "./put.csv"  # The previous CSV
csv_output_path = "./tput.csv"
conflict_report_path = "./report.txt"

# Dictionary to store merged data
merged_data = defaultdict(lambda: defaultdict(set))  # Uses sets to track conflicts

# Read CSV and process rows
with open(csv_input_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    rows = list(reader)

# Process each row
for row in rows:
    key = (row["Id"], row["College Name"], row["Course"])  # Unique identifier for merging

    for col in headers[3:]:  # Ignore first 3 columns (Id, College Name, Course)
        value = row[col].strip()
        if value:
            merged_data[key][col].add(value)  # Store values in a set to track conflicts

# Prepare the final merged dataset
final_data = []
conflict_count = 0
conflict_details = []

for key, values_dict in merged_data.items():
    merged_row = {col: "" for col in headers}  # Initialize empty row
    merged_row["Id"], merged_row["College Name"], merged_row["Course"] = key  # Fill key values

    for col, values in values_dict.items():
        if len(values) == 1:
            merged_row[col] = next(iter(values))  # Single value, no conflict
        else:
            conflict_count += 1
            merged_row[col] = "/".join(sorted(values))  # Join conflicting values
            conflict_details.append(f"Conflict in {col} for {key}: {values}")

    final_data.append(merged_row)

# Write the merged output CSV
with open(csv_output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(final_data)

# Write conflict report
with open(conflict_report_path, "w", encoding="utf-8") as f:
    f.write(f"Total Conflicts Found: {conflict_count}\n")
    f.write("\n".join(conflict_details))

print(f"Merged CSV saved as '{csv_output_path}'")
print(f"Conflict report saved as '{conflict_report_path}'")

