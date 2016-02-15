import sys
import logging
import feedparser
import time

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

from TwitterAPI import TwitterAPI

#logging.basicConfig(
#  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
#  level=logging.DEBUG
#)

if len(sys.argv) != 4:
  print("Usage: rssProducer.py <broker> <topic> <RSS URL>")
  exit(-1)


rss = sys.argv[3]
feed = feedparser.parse(rss)
  # On Clemson Hadoop cluster, we use the Hortonworks port for Kafka: 6667
  #kafka = KafkaClient(sys.argv[1] + ":6667")
#print feed.etag
#print feed.modified
while 1:  
#  producer = SimpleProducer(kafka)
  # production version might need to include Last-Modified check
#  currentStatus = feed['status']
#  if currentStatus == 304:
#    print feed.debug_message
#    continue
#  currentEtag = feed.etag
#  currentModified = feed.modified
#  print (currentEtag)
  for entry in feed['entries']:
    print(entry['title'])
#  feed = feedparser.parse(rss, etag=currentEtag)
#  feed = feedparser.parse(rss, modified=currentModified)
  feed = feedparser.parse(rss)
  print ("=================================================")
  time.sleep(10)
 
#      print(entry['id'])
#      print(entry['updated'])
#      print(entry['updated_parsed'])
#    producer.send_messages(sys.argv[3], Tweet_content + str(datetime.now().time()))

