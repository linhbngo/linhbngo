# linhbngo.github.io

# add the relevant Python modules
pip install --user TwitterAPI
pip install --user kafka-python
pip install --user pyspark

# need to build Spark and Kafka 
./make-distribution.sh --name spark-1.5.2 --tgz -Phadoop-2.2 -Pyarn

# Start Kafka cluster using the default from Quickstart Page of Apache Kafka

# run producer

# run consumer
bin/spark-submit --jars external/kafka-assembly/target/spark-streaming-kafka-assembly_2.10-1.5.2.jar --master spark://<MasterNode>:7077 --driver-memory 10G --executor-memory 10G --executor-cores 10 /home/lngo/git/linhbngo.github.io/repos/python/consumerSpark.py <brokerNode>:2181 <topic>
