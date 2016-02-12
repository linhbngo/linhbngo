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
kafka = KafkaClient(sys.argv[1] + ":6667")
#print feed.etag
#print feed.modified
while 1:  
  producer = SimpleProducer(kafka)
  for entry in feed['entries']:
    #print(entry['title'])
    Reddit_content = "Reddit " + str(entry['title'].encode("utf-8"))
    producer.send_messages(sys.argv[2], Reddit_content)

  feed = feedparser.parse(rss)
 
#  producer.send_messages(sys.argv[2], "Reddit" + entry['title'])
  #print ("=================================================")
  time.sleep(10)
 
#      print(entry['id'])
#      print(entry['updated'])
#      print(entry['updated_parsed'])
#    producer.send_messages(sys.argv[3], Tweet_content + str(datetime.now().time()))

