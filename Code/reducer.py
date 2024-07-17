#!/usr/bin/env python3
import sys 

volume_map = {}
count_map = {}

for line in sys.stdin:
    line = line.strip()

    # Splitting the input line into its components
    year, substring, volumes, count = line.split(',')

    # Creating a tuple key for each year and substring combination
    key = (year, substring)

    # Updating volume and count maps
    volume_map[key] = volume_map.get(key, 0) + int(volumes)
    count_map[key] = count_map.get(key, 0) + int(count)

# Calculating and printing volume averages for each year and substring combination
for key in volume_map.keys():
    volume_average = round(volume_map[key] / count_map[key], 2)
    print(f"{key[0]},{key[1]},{volume_average}")

