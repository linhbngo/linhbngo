import sys
import logging
import happybase

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 5:
  print("Usage: producer.py <broker:port> <topic> <hbase-master> <table-name>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  print("Note: we are using port 9090 for the Thrift API")
  exit(-1)

connection = happybase.Connection(sys.argv[3])

connection.open()

table_list = connection.tables()
print table_list
if (sys.argv[4] in table_list):
    print "Table exists"
else:
    print "Table does not exist. Creating new table ..."
    column_families = {'Raw_Tweets':dict()}
    new_table = connection.create_table(sys.argv[4],column_families)

#kafka = KafkaClient(sys.argv[1])

#print("Connected to broker ...")

#consumer = SimpleConsumer(kafka, "my-group", sys.argv[2])

#print("Start consuming ...")

#for message in consumer:
#    print(message)
