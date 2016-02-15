import sys
import logging
import json
import datetime
import dateutil.parser
import os

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 4:
  print("Usage: producer.py <broker:port> <topic> <path to directory containing data files>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

kafka = KafkaClient(sys.argv[1])
producer = SimpleProducer(kafka)

path = sys.argv[3]
i = 1
start_date = ''
end_date = ''
sleep_time = 0
for filename in os.listdir(path):
  print filename
  for jsonLine in open(os.path.join(path,filename), "r"):
    try:
      d = json.loads(jsonLine)
      jd = json.dumps(d)
      print (str(i) + " " + d['postedTime'])
      if i == 1:
        sleep_time = 0
        start_date = dateutil.parser.parse(d['postedTime'])
      else:
        end_date = dateutil.parser.parse(d['postedTime'])
        delta = end_date - start_date
        sleep_time = delta.total_seconds()
        start_date = end_date
        print(sleep_time)
      i += 1
      producer.send_messages(sys.argv[2], jd)
    except ValueError, ReaderError:
      print "Ooops, bad line"
      print "-" + jsonLine + "-"
#  with gzip.open(os.path.join(path,filename), "rb") as f:
#    print f
#    twitData = json.loads(f.read().decode("ascii"))
#    print twitData
#  if 'text' in item:
#    print(str(i) + " " + item[
