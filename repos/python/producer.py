import sys
import logging

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

from TwitterAPI import TwitterAPI

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 5:
  print("Usage: producer.py <broker:port> <track-term> <topic> <key location>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

TRACK_TERM = sys.argv[2]

# read keys from external file (not on github)
keyFile = open(sys.argv[4],"r")
CONSUMER_KEY = keyFile.readline().rstrip()
CONSUMER_SECRET = keyFile.readline().rstrip()
ACCESS_TOKEN_KEY = keyFile.readline().rstrip()
ACCESS_TOKEN_SECRET = keyFile.readline().rstrip()

print(CONSUMER_KEY)
print(CONSUMER_SECRET)
print(ACCESS_TOKEN_KEY)
print(ACCESS_TOKEN_SECRET)

api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track': TRACK_TERM})

kafka = KafkaClient(sys.argv[1])

producer = SimpleProducer(kafka)
i=1
for item in r:
  if 'text' in item:
    print(str(i) + " " + item['text'])
    Tweet_content = str(i) + " " + str(item['text'].encode("utf-8"))
    producer.send_messages(sys.argv[3], Tweet_content + str(datetime.now().time()) )
    i += 1
