import re
import csv

# Path to the extracted text file and output CSV file
text_file_path = "extracted_text.txt"
csv_file_path = "output.csv"

# Read the extracted text from the file
with open(text_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Initialize storage structures
structured_data = []
current_college = None
current_course = None

# Define column headers based on available categories in the text
headers = ["Id", "College Name", "Course", "GOPENS", "GSCS", "GSTS", "GVJS", "GNT1S", "GNT2S", "GNT3S",
           "GOBCS", "LOPENS", "LSCS", "LSTS", "LVJS", "LNT1S", "LNT2S", "LNT3S", "LOBCS", "PWDOPENS",
           "DEFOPENS", "TFWS", "PWDROBC", "DEFROBCS", "DEFRSCS", "EWS"]

# Iterate through each line and extract information
for line in lines:
    line = line.strip()
    
    # Match college name
    college_match = re.match(r"(\d{4}) - (.+)", line)
    if college_match:
        current_college = college_match.group(2)
        continue

    # Match course
    course_match = re.match(r"(\d{9}) - (.+)", line)
    if course_match:
        current_course = course_match.group(2)
        course_id = course_match.group(1)
        continue

    # Match seat category and cutoff values
    if re.match(r"^\s*I\s+", line):
        values = re.findall(r"(\d+)", line)  # Extract numeric cutoffs
        row = [course_id, current_college, current_course] + values[:len(headers) - 3]  # Limit to expected headers
        structured_data.append(row)

# Write to CSV
with open(csv_file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(structured_data)

print(f"CSV file has been created: {csv_file_path}")

