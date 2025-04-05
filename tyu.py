import pdfplumber
import csv

# Path to the uploaded PDF file
pdf_path = "/home/manth/Downloads/mhtcetcell/2022ENGG_CAP1_CutOff.pdf"
csv_path = "./output.csv"

# Extract text from PDF
data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            data.append(text)

# Save extracted text to analyze structure
extracted_text = "\n".join(data)

# Save extracted text for review (if needed)
text_output_path = "./extracted_text.txt"
with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)


import re

# Split the extracted text into lines
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
    elif line.startswith("  I "):  # Seat category data starts with "  I "
        values = re.findall(r"(\d+)", line)  # Extract all numbers
        row = [course_id, current_college, current_course] + values
        structured_data.append(row)

# Save to CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(structured_data)

csv_path
