import sys
import logging
import urllib
import os

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 4:
  print("Usage: producer.py <broker:port> <topic> <photo directory>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

kafka = KafkaClient(sys.argv[1])

print("Connected to broker ...")

consumer = SimpleConsumer(kafka, "my-group", sys.argv[2])

print("Start consuming ...")

i = 1
for message in consumer:
  print(message.message)
  photo_url = message.message.value
  file_name = os.path.join(sys.argv[3],str(i)) + '.' + photo_url.split('.')[-1]
  urllib.urlretrieve(photo_url, file_name)
  i += 1
