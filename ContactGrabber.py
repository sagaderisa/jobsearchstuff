
# Program to grab contacts for companies from LinkedIn contacts CSVs


# This program was written by ChatGPT based on the following prompt:
# Please write a program that will:
# 1) take a list of companies in an Excel file from a worksheet called "Companies" and 
# 2) look through multiple LinkedIn Connection CSV files and find any connections from that company. Pull the connection's name and title.
# 3) Add each connection to the Excel file into a worksheet called "Contacts." 

import pandas as pd
from openpyxl import load_workbook

# 1. Load the companies from the Excel file
excel_file = '/Users/bethanyquinn/Documents/Python Files/Crunchbase Financed Cos.xlsx'
df_companies = pd.read_excel(excel_file, sheet_name='Companies')

# Convert the companies to a set for faster searching
companies = set(df_companies['Company'].str.lower())

# Prepare a DataFrame to store contacts
df_contacts = pd.DataFrame(columns=['Company', 'FirstName', 'LastName', 'Position'])

# 2. Loop through your LinkedIn CSV files
csv_files = ['/Users/bethanyquinn/Documents/Python Files/BQLinkedInConnections.csv']  # Add your file names here
for csv_file in csv_files:
    df_connections = pd.read_csv(csv_file)
    df_connections['Company'] = df_connections['Company'].str.lower()
    
    # Find the matching connections
    matches = df_connections['Company'].isin(companies)
    df_matched_connections = df_connections[matches]
    
    # Append to the contacts DataFrame
    df_contacts = pd.concat([df_contacts, df_matched_connections])

# 3. Write the contacts to the Excel file
with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a') as writer:
    df_contacts.to_excel(writer, sheet_name='Contacts', index=False)
