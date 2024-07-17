# README: MapReduce Use Case - Jakob Kuemmerle

## MapReduce Program for Analyzing Google Books Data 

### Implementation of Q1:
#### mapper.py:
- Analyzes each input line, extracting relevant information such as year, volumes, and words.
- Calculates volumes for specified keywords ('nu', 'chi', 'haw') based on their occurrences in the line.
- Prints the year, keyword, volume, and count to stdout.

#### reducer.py:
- Aggregates volumes and counts for each year and substring combination.
- Calculates the volume average for each year and substring combination.
- Prints the year, substring, and volume average to stdout.

#### run.sh:
- Shell script to execute the MapReduce job using Hadoop Streaming.
- Specifies input paths for both "google_1gram" and "google_2gram" datasets.
- Specifies the output path for the results.
- Uses Hadoop Streaming jar to run the mapper and reducer Python scripts.

### Usage:
1. Ensure that the input datasets ("google_1gram" and "google_2gram") are stored in HDFS.
2. Execute the `run.sh` script to run the MapReduce job.
3. Check the `output.txt` in the specified output directory for the calculated volume averages.
