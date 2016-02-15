#!/bin/bash
spark-submit \
  --conf spark.root.logger=WARN,console \
  --master yarn-cluster \
  --jars ../lib/spark-streaming-kafka_2.10-1.3.1.2.3.0.0-2557.jar,/home/lngo/software/kafka_2.10-0.8.2.2/libs/kafka_2.10-0.8.2.2.jar,/home/lngo/software/kafka_2.10-0.8.2.2/libs/zkclient-0.3.jar,/home/lngo/software/kafka_2.10-0.8.2.2/libs/metrics-core-2.2.0.jar,/home/lngo/software/kafka_2.10-0.8.2.2/libs/kafka-clients-0.8.2.2.jar \
  consumerSpark.py namenode1.palmetto.clemson.edu:2181 ClemsonTopic
