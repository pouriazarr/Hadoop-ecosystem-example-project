uber_data = LOAD 'hdfs://namenode:9000/user/root/pigoutput100/part-m-00000' AS (date:chararray, time:chararray, address:chararray);
fuber_data = FILTER uber_data BY date == '9/30/2014';
guber_data = GROUP fuber_data BY address;
STORE guber_data INTO 'hdfs://namenode:9000/user/root/pigoutput110' USING PigStorage(',');