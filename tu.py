import pdfplumber
import csv

import re

# Path to the uploaded PDF file
pdf_path = "/home/manth/Downloads/mhtcetcell/2021ENGG_CAP1_CutOff.pdf"
csv_path = "./out.csv"

# Read input data from the file
with open("./extracted_text.txt", "r", encoding="utf-8") as file:
    extracted_text = file.read()

print(extracted_text)

lines = extracted_text.split("\n")

# Initialize variables
structured_data = []
current_college = None
current_course = None

# Define column headers (as seen in the extracted text)
headers = ["Id", "College Name", "Course", "GOPENS", "GSCS", "GSTS", "GVJS", "GNT1S", "GNT2S", "GNT3S",
           "GOBCS", "LOPENS", "LSCS", "LSTS", "LVJS", "LNT1S", "LNT2S", "LNT3S", "LOBCS", "PWDOPENS",
           "DEFOPENS", "TFWS", "EWS"]

# Regex patterns
college_pattern = re.compile(r"(\d{4}) - (.+)")
course_pattern = re.compile(r"(\d{9}) - (.+)")

# Process each line
for line in lines:
    college_match = college_pattern.match(line.strip())
    course_match = course_pattern.match(line.strip())

    if college_match:
        current_college = college_match.group(2)
    elif course_match:
        current_course = course_match.group(2)
        course_id = course_match.group(1)
    elif line.startswith("I "):  # Seat category data starts with "  I "
        values = re.findall(r"(\d+)", line)  # Extract all numbers
        row = [course_id, current_college, current_course] + values
        structured_data.append(row)

print(structured_data)

# Save to CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(structured_data)
