#!/bin/bash
classname=$1
sourcefile="$classname.java"
jarfile="$classname.jar"

rm -Rf classes
rm $jarfile
mkdir classes

export HADOOP_HOME="/usr/hdp/current/"
export HADOOP_COMMON_HOME="${HADOOP_HOME}/hadoop-client"
export HADOOP_MAPRED_HOME="${HADOOP_HOME}/hadoop-mapreduce-client"
export YARN_HOME="${HADOOP_HOME}/share/hadoop/yarn-client"
export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk.x86_64"


echo "Compiling ..."
javac -cp "$HADOOP_COMMON_HOME/*:$HADOOP_MAPRED_HOME/*" -d classes $sourcefile

echo "Creating jar ..."
jar -cvf $jarfile -C classes/ .

echo "Executing ..."
#java -cp $jarfile:$HADOOP_COMMON_HOME/hadoop-common-2.6.0.jar:$HADOOP_COMMON_HOME/lib/*:$HADOOP_MAPRED_HOME/hadoop-mapreduce-client-core-2.6.0.jar:$HADOOP_MAPRED_HOME/hadoop-mapreduce-client-jobclient-2.6.0.jar:$HADOOP_MAPRED_HOME/hadoop-mapreduce-client-shuffle-2.6.0.jar:$HADOOP_MAPRED_HOME/hadoop-mapreduce-client-common-2.6.0.jar:$YARN_HOME/*:. $1 $2 $3
