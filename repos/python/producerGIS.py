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

if len(sys.argv) != 4:
  print("Usage: producer.py <broker:port> <topic> <key location>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

# read keys from external file (not on github)
keyFile = open(sys.argv[3],"r")
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
# use openstreetmaip.org to find bounding box covering highschoool area - Export tab. 
# Coordinates should go counter clockwise

# example: bounding box for New York
#r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})

# example: Clemson University
r = api.request('statuses/filter',{'locations':'-82.85,34.66,-82.81,34.69'})
kafka = KafkaClient(sys.argv[1])

producer = SimpleProducer(kafka)
i=1
for item in r.get_iterator():
  print "=================================================="
  if 'entities' in item:
    if 'media' in item['entities']:
      for media in item['entities'].get('media'):
        if media['type'] == 'photo':
          photo_url = media['media_url_https']
          print photo_url
          screen_name = item['user']['screen_name']
          print screen_name
          producer.send_messages(sys.argv[2], str(photo_url))
  if 'text' in item:
#    print(str(i) + " " + item['text'])
    Tweet_content = str(i) + " " + str(item['text'].encode("utf-8"))
#    producer.send_messages(sys.argv[2], Tweet_content + str(datetime.now().time()) )
    i += 1
