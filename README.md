# NYC-TRAFFIC-DATA-ANALYSIS

This dataset was collected from the City of New York’s data website, and contains all reports of vehicular incidents in New York City over a period of time. The file is roughly 175MB in size, and contains over 900,000 records. 

The dataset can be downloaded from 
https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95

There are a considerable number of fields, including columns with a common format that describe up to 5 vehicles that contributed to the particular incident. 
 
 
## ANALYSIS

Using the Hadoop streaming API, built mapper and reducer scripts that analyze the data and yield summary counts for each vehicle that 
describe the total count, per vehicle type, that the vehicle type was involved in an incident. If the same type of vehicle was involved more than once in an incident, then it has been counted twice for the purpose of summary statistic.

## STEPS TO RUN THE MAPPER AND REDUCER CODE

1. Copy the given Mapper.py and Reducer.py files in Edge Node.
2. Download the nyc-traffic-collision dataset from given link and copy it into HDFS location.
3. Using below command run the scripts and generate a statistics file on HDFS and log file on edge node.

### Command to run Mapper and Reducer scripts

The given command would write final statistics in HDFS location and also generate a log file in home directory of Edge node.

    hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -file <EDGE_NODE_PATH_FOR_MAPPER_SCRIPT> -mapper  <EDGE_NODE_PATH_FOR_MAPPER_SCRIPT> -file <EDGE_NODE_PATH_FOR_REDUCER_SCRIPT> -mapper  <EDGE_NODE_PATH_FOR_REDUCER_SCRIPT> -input <HDFS_PATH_FOR_NYC_DATASET> -output <HDFS_PATH_FOR_FINAL_OUTPUT> 2>> <EDGE_NODE_PATH_FOR WRITING_JOB_LOG>

Sample command to run job

    hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar  -file /home/gupta2su/mapper.py  -mapper /home/gupta2su/mapper.py  -file /home/gupta2su/ reducer.py  -reducer /home/gupta2su/reducer.py  -input /user/tatavag/nyc.data -output cloud_hw4/mapper_output_20190423 2>> gupta_shubham_job_log.txt
