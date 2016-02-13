import sys
import logging
import happybase
import ast

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

current_table = connection.table(sys.argv[4])

kafka = KafkaClient(sys.argv[1])

print("Connected to broker ...")

consumer = SimpleConsumer(kafka, "my-group", sys.argv[2])

print("Start consuming ...")

# set up batch

msg_batch = table.batch()
msg_counter = 1

for message in consumer:
    e = ast.literal_eval(message.message.value)
    # generate row key

    if msg_counter <= 1000:
        # call msg_batch.put('row-key', {'cf:col1': 'value1','cf:col2': 'value2'})
        # or msg_batch.put('row-key', {'cf:col1': 'value1'}, timestamp=123456789)

        msg_counter += 1
    else:
        msg_batch.send()
        msg_counter = 1
