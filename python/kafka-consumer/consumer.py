import sys
import logging
import json
import ast

from kafka import KafkaConsumer

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 3:
  print("Usage: producer.py <broker:port> <topic>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

consumer = KafkaConsumer(bootstrap_servers=sys.argv[1], auto_offset_reset='latest')
consumer.subscribe([sys.argv[2]])

print("Start consuming ...")

for message in consumer:
  e = json.loads(json.loads(message.value.encode('utf-8')))
  print ("------")
  print type(e)
  if u'id' in e:
    print (e[u'id'])
  else:
    print ("Hit rate limit ...")
  print("======== \n")
