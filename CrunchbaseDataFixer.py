# Crunchbase Data Fixer

# When you copy Crunchbase data it comes out in one column, so this program fixes that.

import csv

# Define the headers
headers = ['Organization Name', 'Actively Hiring', 'Number of Employees', 'Last Funding Date', 
           'Last Funding Type', 'Founded Date', 'Industries', 'Headquarters Location', 
           'Description', 'CB Rank']

# Read the data from a file
with open('CrunchbaseCos.txt', 'r') as f:
    data = f.read()

# Split the data into records
records = data.split("\n\n")

# Split each record into its components
records = [rec.split("\n") for rec in records]

# Write records to a CSV file
with open('UpdatedCompaniesToPaste.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # Write headers
    for rec in records:
        writer.writerow(rec)
