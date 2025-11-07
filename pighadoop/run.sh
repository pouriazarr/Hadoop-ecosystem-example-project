#!/bin/bash
pig -x mapreduce /home/app/filter_and_store_data.pig
hdfs dfs -get /user/root/pigoutput110
python /home/app/analyse_uber_data.py
tail -f /dev/null