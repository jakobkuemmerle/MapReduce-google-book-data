#!/usr/bin/env python3
import sys
import re 

keywords = ['nu', 'chi', 'haw']

def analyze_input_line(line_parts):
    """Analyze each line, extract relevant information, and calculate volumes for keywords"""

    # Extract year, volumes, and words from the line
    volumes = int(line_parts[-1])
    year = line_parts[-3]
    words = line_parts[:-3]

    # Skip the line if the year is not numeric
    if not year.isnumeric():
        return
    
    year = int(year)
    # Process the line if the year is within a valid range (before 2024)
    if year <= 2024:
        for keyword in keywords:
            count = sum([keyword in word.lower() for word in words])
            if count > 0:
                volume_for_keyword = count * volumes
                print(f"{year},{keyword},{volume_for_keyword},{count}")

# Main processing loop
for input_line in sys.stdin:
    input_line = input_line.strip()
    line_parts = re.split(r'\s+', input_line)
    
    # Check if the line has a valid number of parts
    if len(line_parts) < 4 or len(line_parts) > 5:
        continue 
    analyze_input_line(line_parts)

