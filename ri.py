import csv
import re

# Path to the extracted text file
text_file_path = "./extracted_text.txt"
csv_output_path = "./put.csv"

# Read extracted text from file
with open(text_file_path, "r", encoding="utf-8") as f:
    extracted_text = f.read()

# Split text into lines
lines = extracted_text.split("\n")

# Initialize variables
structured_data = []
current_college = None
current_course = None
all_headers = set()
table_data = []

# Regex patterns
college_pattern = re.compile(r"(\d{4}) - (.+)")
course_pattern = re.compile(r"(\d{9}) - (.+)")
stage_pattern = re.compile(r"Stage\s+(.+)")
cutoff_pattern = re.compile(r"(\d+)")

# First pass: Collect all possible headers
for line in lines:
    stage_match = stage_pattern.match(line.strip())
    if stage_match:
        headers = stage_match.group(1).split()
        all_headers.update(headers)

# Convert to sorted list for consistency
sorted_headers = sorted(all_headers)
final_headers = ["Id", "College Name", "Course"] + sorted_headers

# Second pass: Extract structured data
for i, line in enumerate(lines):
    college_match = college_pattern.match(line.strip())
    course_match = course_pattern.match(line.strip())
    stage_match = stage_pattern.match(line.strip())

    if college_match:
        current_college = college_match.group(2)
    elif course_match:
        current_course = course_match.group(2)
        course_id = course_match.group(1)
    elif stage_match:
        current_headers = stage_match.group(1).split()
    elif line.startswith("I "):
        values = cutoff_pattern.findall(line)
        row = {header: "" for header in final_headers}  # Initialize empty row

        row["Id"] = course_id
        row["College Name"] = current_college
        row["Course"] = current_course

        # Fill available columns
        for j, value in enumerate(values):
            if j < len(current_headers):
                row[current_headers[j]] = value  # Only fill the present columns

        table_data.append(row)

# Write to CSV
with open(csv_output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=final_headers)
    writer.writeheader()
    writer.writerows(table_data)

print(f"CSV file '{csv_output_path}' generated successfully!")

