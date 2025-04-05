import csv
import re

# Define input and output file names
input_file = "./extracted_text.txt"  # Replace with your actual input file
output_file = "cutoff_list.csv"

# Regular expression pattern to extract relevant data
pattern = re.compile(
    r"(\d+)\s+\(([\d\.]+)\)\s+(\d+)\s+([\d-]+)\s+-\s+([^,]+),?\s*(.*?)\s+JEE\(Main\)\s+AI to AI\s+AI"
)

# Read the input file and extract data
data = []
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            sr_no, merit, percentile, choice_code, institute, course = match.groups()
            data.append([sr_no, merit, percentile, choice_code, institute.strip(), course.strip()])

# Write the extracted data to a CSV file
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sr. No", "All India Merit", "Percentile", "Choice Code", "Institute Name", "Course Name"])
    writer.writerows(data)

print(f"CSV file '{output_file}' has been created successfully!")
