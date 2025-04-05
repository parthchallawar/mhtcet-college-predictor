import pdfplumber
import csv

# Path to the uploaded PDF file
# pdf_path = "./2020ENGG_CAP1_AI_CutOff.pdf"
pdf_path = "/home/manth/Downloads/mhtcetcell/2024ENGG_CAP1_CutOff.pdf"
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
text_output_path = "./extracted_textt.txt"
with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)

