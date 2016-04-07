import sys
import logging
import json

from kafka import KafkaProducer
from datetime import datetime

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

class StdOutListener(StreamListener):
  def on_data(self, data):
    producer.send(sys.argv[2], json.dumps(data))
    return True

  def on_error(self, status):
    print status

if len(sys.argv) != 4:
  print("Usage: producer.py <broker:port> <topic> <key location>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  exit(-1)

producer = KafkaProducer(bootstrap_servers=sys.argv[1])

# read keys from external file (not on github)
keyFile = open(sys.argv[3],"r")
CONSUMER_KEY = keyFile.readline().rstrip()
CONSUMER_SECRET = keyFile.readline().rstrip()
ACCESS_TOKEN_KEY = keyFile.readline().rstrip()
ACCESS_TOKEN_SECRET = keyFile.readline().rstrip()

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
while True:
  try:
    stream = Stream(auth, StdOutListener())
    stream.filter(track=["Hillary","Clinton","ImWithHer","Hillary2016","HillaryForAmerica","realDonaldTrump","Trump","TrumpNewMedia","Trump2016","MakeAmericaGreatAgain","ChooseCruz","tedcruz","CruzCrew","CruzToVictory","Cruz2016","BernieSanders","FeelTheBern","Bernie","bernie2016","Sanders","Elections2016","Decision2016"])
  except IncompleteRead:
    print ("Lets try it again")
    continue
  except KeyboardInterrupt:
    stream.disconnect()
    break
