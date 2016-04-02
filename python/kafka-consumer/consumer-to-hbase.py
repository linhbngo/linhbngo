import sys
import logging
import happybase
import json

from kafka import KafkaConsumer

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
  column_families = {'Raw_Tweets:json':dict()}
  new_table = connection.create_table(sys.argv[4],column_families)

current_table = connection.table(sys.argv[4])

consumer = KafkaConsumer(bootstrap_servers=sys.argv[1], auto_offset_reset='latest')
consumer.subscribe([sys.argv[2]])
print("Start consuming ...")

# set up batch

msg_batch = current_table.batch()
msg_counter = 0

for message in consumer:
  # print message.message.value
  d = json.loads(json.loads(message.value.encode('utf-8')))
  # generate row key
  # print d
  if u'id' in d:
    row_key = d[u'id']
    #print str(msg_counter) + ": " + str(row_key)
    if msg_counter >= 1000:
      # call msg_batch.put('row-key', {'cf:col1': 'value1','cf:col2': 'value2'})
      #print "Stop the batch at 10000 tweets to send to HBase"
      msg_batch.send()
      msg_counter = 1
    else:
      msg_batch.put(str(row_key), {'Raw_Tweets:json': message.value.encode('utf-8')})
      msg_counter += 1
connection.close()
