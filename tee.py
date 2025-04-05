import csv
import re

# Read input data from the file
with open("extracted_text.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(len(data))

# Regular expressions to capture required fields
college_pattern = re.compile(r"(\d{4}) - (.*?)\n")  # College Code and Name
branch_pattern = re.compile(r"(\d{9}) - (.*?)\n")  # Branch Code and Name
quota_pattern = re.compile(r"(State Level|Home University|Other than Home University)")  # Quota Type
cutoff_pattern = re.compile(r"([A-Z]+) (\d+)\s*\(([\d.]+)\)")  # Seat Type, Merit Number, Percentile/Score

# Output file
csv_filename = "cutoff_data.csv"

# Process and extract data
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write headers
    writer.writerow(["College Code", "College Name", "Branch Code", "Branch Name", 
                     "Quota Category", "Stage", "Seat Type", "Cutoff Merit No", "Score/Percentile"])
    
    lines = data.split("\n")
    current_college = None
    current_branch = None
    current_quota = None

    for line in lines:
        college_match = college_pattern.match(line)
        branch_match = branch_pattern.match(line)
        quota_match = quota_pattern.search(line)

        if college_match:
            current_college = college_match.groups()
        
        elif branch_match:
            current_branch = branch_match.groups()
        
        elif quota_match:
            current_quota = quota_match.group()

        elif "Stage" in line:
            current_stage = line.strip().split()[1]  # Extracts Stage (e.g., "I")
        
        else:
            for match in cutoff_pattern.finditer(line):
                seat_type, merit_no, score = match.groups()
                writer.writerow([
                    current_college[0], current_college[1],
                    current_branch[0], current_branch[1],
                    current_quota, current_stage,
                    seat_type, merit_no, score
                ])

print(f"CSV file '{csv_filename}' generated successfully!")
