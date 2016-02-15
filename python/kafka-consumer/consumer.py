import sys
import logging
import json
import yaml
import ast

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 3:
  print("Usage: producer.py <broker:port> <topic>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

kafka = KafkaClient(sys.argv[1])

print("Connected to broker ...")

consumer = SimpleConsumer(kafka, "my-group", sys.argv[2])

print("Start consuming ...")

for message in consumer:
    # the content sent from the producer cannot be parsed into a JSON object.
    # this code settles with converting it into a python dict obect instead.
    e = ast.literal_eval(message.message.value)
    #print d
    print ("\n")
    print e[u'text'].encode("utf-8")
    #print(message.message)
    #print(d)
    print("======== \n")
    #print d
