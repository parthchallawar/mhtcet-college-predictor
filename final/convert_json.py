import csv
import json

input_file = './merged_output.csv'  # or .tsv if needed
output_file = 'admission_data.json'

data = []

with open(input_file, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    
    for row in reader:
        # print(row)
        # Convert fields to appropriate types
        try:
            entry = {
                'collegeid': str(row['collegeid']),
                'college_name': row['college name'],
                'course': row['course'],
                'merit_number': int(float(row['merit number'])),  # Handles both float and int format
                'seat_type': row['seat type'],
                'percentile': float(row['percentile']),
                'academic_year': int(row['Academic Year']),
                'cap_round': row['Cap Round'],
                'college_type': row.get('college type', 'Unknown')  # Just in case it's included
            }
            data.append(entry)
        except:
            print("Ignored")
            

# Write to JSON
with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"✅ Converted {len(data)} records to {output_file}")
