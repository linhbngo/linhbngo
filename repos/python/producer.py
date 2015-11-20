import sys

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

from TwitterAPI import TwitterAPI

if len(sys.argv) != 4:
  print("Usage: producer.py <broker> <track-term> <topic>")
  exit(-1)

#TRACK_TERM = 'Clemson'
TRACK_TERM = sys.argv[2]

CONSUMER_KEY = 'yXmWAkCKfUTXpxakMqJxy8NuH'
CONSUMER_SECRET = 'xBfst9PYhkpwv3X3WdhuBsJHwf9fUEBuHPGz1NJikjw025odDh'
ACCESS_TOKEN_KEY = '374741989-xGscbglKIEFMY7MTch2vPF6qsOKsV3U7qt24k0wb'
ACCESS_TOKEN_SECRET = 'QWLwpPFGsZ2pwbe3dxxAsLzTl9s0jF1qeQjSbl0vZcG5g'


api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track': TRACK_TERM})

kafka = KafkaClient(sys.argv[1] + ":9092")

producer = SimpleProducer(kafka)
i=1
for item in r:
  if 'text' in item:
    print(str(i) + " " + item['text'])
    Tweet_content = str(i) + " " + str(item['text'].encode("utf-8"))
    producer.send_messages(sys.argv[3], Tweet_content + str(datetime.now().time()) )
    i += 1
#  else:
#    producer.send_messages("test", item + str(datetime.now().time()) )
