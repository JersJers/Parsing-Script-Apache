import re

# Define the regular expression for parsing log entries
log_pattern = r"\[(.*?)\] \[(.*?)\] \[client.*?\] (.*)"

# Function to parse a single log entry
def parse_log_entry(entry):
    match = re.search(log_pattern, entry)
    if match:
        return {
            'timestamp': match.group(1),
            'error_level': match.group(2),
            'message': match.group(3)
        }
    return None

# Function to read and parse the entire log file
def parse_log_file(file_path):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            parsed_data = parse_log_entry(line)
            if parsed_data:
                results.append(parsed_data)
    return results

# Path to the log file
log_file_path = 'Apache_2k.log'  # Adjust the path as needed for your environment

# Parse the log file and print the results
parsed_entries = parse_log_file(log_file_path)
for entry in parsed_entries:
    print(entry)