import pdfplumber
import csv
import re

# Path to the extracted text file (replace with your actual file path)
text_file_path = "./extracted_text.txt"
csv_output_path = "./goutput.csv"

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

# Regex patterns
college_pattern = re.compile(r"(\d{4}) - (.+)")
course_pattern = re.compile(r"(\d{9}) - (.+)")
stage_pattern = re.compile(r"Stage\s+(.+)")  # Captures all seat categories after "Stage"

# First pass: Collect all possible headers
for line in lines:
    stage_match = stage_pattern.match(line.strip())
    if stage_match:
        headers = stage_match.group(1).split()  # Extracts seat categories
        all_headers.update(headers)

# Convert to sorted list for consistency
sorted_headers = sorted(all_headers)

# Define final column headers dynamically
headers = ["Id", "College Name", "Course"] + sorted_headers

# Second pass: Extract structured data
for i, line in enumerate(lines):
    college_match = college_pattern.match(line.strip())
    course_match = course_pattern.match(line.strip())

    if college_match:
        current_college = college_match.group(2)
    elif course_match:
        current_course = course_match.group(2)
        course_id = course_match.group(1)
    elif line.startswith("I "):  # Identifying cutoff values
        values = re.findall(r"(\d+)", line)  # Extract all numbers
        row = {header: "" for header in headers}  # Initialize empty row
        row["Id"] = course_id
        row["College Name"] = current_college
        row["Course"] = current_course

        # Fill seat type values in order
        for j, value in enumerate(values):
            if j < len(sorted_headers):
                row[sorted_headers[j]] = value

        structured_data.append(row)

# Save to CSV
with open(csv_output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(structured_data)

print(f"CSV file '{csv_output_path}' generated successfully!")
