#!/usr/bin/python3
"""Log parsing"""
import sys

# Initialize variables for statistics
total_file_size = 0
status_code_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()

        # Parse the input line
        try:
            parsed_line = line.split()
            status_code = int(parsed_line[-2])
            file_size = int(parsed_line[-1])
        except (ValueError, IndexError):
            continue

        # Update statistics
        total_file_size += file_size
        try:
            status_code_counts[status_code] += 1
        except KeyError:
            continue

        # Print statistics every 10 lines
        if line_number % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code, count in status_code_counts.items():
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code, count in status_code_counts.items():
        if count > 0:
            print("{}: {}".format(code, count))
