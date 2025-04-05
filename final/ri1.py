import csv
import re

text_file_path = "./extracted_textt.txt"
csv_output_path = "./rput.csv"

with open(text_file_path, "r", encoding="utf-8") as f:
    extracted_text = f.read()

lines = extracted_text.split("\n")

structured_data = []
current_college = None
current_course = None
all_headers = set()
table_data = []

college_pattern = re.compile(r"(\d{4}) - (.+)")
course_pattern = re.compile(r"(\d{9}) - (.+)")
stage_pattern = re.compile(r"Stage\s+(.+)")
cutoff_pattern = re.compile(r"(\d+)")
percentile_pattern = re.compile(r"\(([\d.]+)\)")  # Regex to capture percentile values

for line in lines:
    stage_match = stage_pattern.match(line.strip())
    if stage_match:
        headers = stage_match.group(1).split()
        all_headers.update(headers)

sorted_headers = sorted(all_headers)
final_headers = ["Id", "College Name", "Course"] + sorted_headers + [f"{header}_Percentile" for header in sorted_headers]

i = 0
while i < len(lines):
    line = lines[i].strip()
    college_match = college_pattern.match(line)
    course_match = course_pattern.match(line)
    stage_match = stage_pattern.match(line)

    if college_match:
        current_college = college_match.group(2)
    elif course_match:
        current_course = course_match.group(2)
        course_id = course_match.group(1)
    elif stage_match:
        current_headers = stage_match.group(1).split()
    elif line.startswith("I "):
        values = cutoff_pattern.findall(line)
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            percentiles = percentile_pattern.findall(next_line)
        else:
            percentiles = []

        row = {header: "" for header in final_headers}  # Initialize empty row

        row["Id"] = course_id
        row["College Name"] = current_college
        row["Course"] = current_course

        for j, value in enumerate(values):
            if j < len(current_headers):
                row[current_headers[j]] = value

        for j, percentile in enumerate(percentiles):
            if j < len(current_headers):
                row[f"{current_headers[j]}_Percentile"] = percentile  # Fill percentiles

        table_data.append(row)
        i += 1

    i += 1

with open(csv_output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=final_headers)
    writer.writeheader()
    writer.writerows(table_data)

print(f"CSV file '{csv_output_path}' generated successfully!")
