#!/bin/bash

input_path1="hw2/google/google_1gram" # in hdfs
input_path2="hw2/google/google_2gram" # in hdfs
output_path="hw2/output1" # in hdfs and must not exist
python_path=$(pwd)
hadoop_lib_path="/opt/hadoop/hadoop/share/hadoop/tools/lib"

yarn jar ${hadoop_lib_path}/hadoop-streaming-2.10.1.jar \
       -files ${python_path}/mapper.py,${python_path}/reducer.py \
    -input ${input_path1},${input_path2} \
    -output ${output_path} \
    -mapper 'python3 mapper.py' \
    -reducer 'python3 reducer.py'

