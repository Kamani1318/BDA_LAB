# For Streaming Purposes
hadoop jar /home/hdoop/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \
    -file mapper.py -mapper mapper.py \
    -file reducer.py -reducer reducer.py \
    -input /path/to/student_data.txt -output /path/to/output_directory
