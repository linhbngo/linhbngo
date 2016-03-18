#!/bin/bash
echo "Test for HDFS output directory existence ..."
hdfs dfs -test -d /user/lngo/outputTwitter
echo $?
if [ $? == 0 ]; then
  hdfs dfs -rm -f -r /user/lngo/outputTwitter    
fi

echo "Executing ..."
yarn jar Kafka-Streaming-Twitter/target/Kafka-Streaming-Twitter-0.0.1-SNAPSHOT.jar org.lngo.kafkastreamingtwitter.TwitterJavaProducer hdfs:///user/lngo/cert/Twitter /user/lngo/outputTwitter

