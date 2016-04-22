import sys
import happybase
import json

from kafka import KafkaConsumer


if len(sys.argv) != 5:
  print("Usage: producer.py <broker:port> <topic> <hbase-master> <table-name>")
  print("Note: use port 9092 for default Kafka broker and 6667 for HDP Kafka broker")
  print("Note: we are using port 9090 for the Thrift API")
  exit(-1)

connection = happybase.Connection(sys.argv[3])

connection.open()

table_list = connection.tables()
print table_list
if (sys.argv[4] in table_list):
  print "Table exists"
else:
  print "Table does not exist. Creating new table ..."
  column_families = {'Raw_Tweets:json':dict()}
  new_table = connection.create_table(sys.argv[4],column_families)

current_table = connection.table(sys.argv[4])

consumer = KafkaConsumer(bootstrap_servers=sys.argv[1], auto_offset_reset='latest')
consumer.subscribe([sys.argv[2]])
print("Start consuming ...")

# set up batch

msg_batch = current_table.batch()
msg_counter = 0

for message in consumer:
  # print message.message.value
  d = json.loads(json.loads(message.value.encode('utf-8')))
  # generate row key
  # print d
  if u'id' in d:
    row_key = d[u'id']
    print "ID: ", d[u'id']
    if u'annotations' in d:
      print "Annotations: ", d[u'annotations']
    print "Contributors:", d[u'contributors']
    print "Coordinates: ", d[u'coordinates']

    print "Created at: ", d[u'created_at']
    if u'current_user_retweet' in d:
      print "Current User Retweet: ", d[u'current_user_retweet']
    print "Entities: ", 
    print "  User_mentions:", d[u'entities'][u'user_mentions']
    print "  Symbols: ", d[u'entities'][u'symbols']
    print "  Hashtags: ", d[u'entities'][u'hashtags']
    print "  URLs: ", d[u'entities'][u'urls']
    print "Favorites Count: ", d[u'favorite_count']
    print "Favorited: ", d[u'favorited']
    print "Filter Level: ", d[u'filter_level']
    print "Geo: ", d[u'geo']
    print "Reply to screen name: ", d[u'in_reply_to_screen_name']
    print "Reply to status ID: ", d[u'in_reply_to_status_id']
    print d[u'in_reply_to_status_id_str']
    print "Reply to user ID: ", d[u'in_reply_to_user_id']
    print d[u'in_reply_to_user_id_str']
    print "Language: ", d[u'lang']
    print "Place: ", d[u'place']   
    if u'Possibly Sensitive' in d:                  
      print "Possibly Sensitive: ", d[u'possibly_sensitive']
    if u'quoted_status_id' in d:
      print "Quoted Status ID: ",d[u'quoted_status_id']
    if u'is_quoted_status' in d:
     print "Is quoted: ", d[u'is_quoted_status']
    if u'scopes' in d:
      print "Scopes: ", d[u'scopes']
    print "Retweet count:", d[u'retweet_count']
    print "Retweeted: ", d[u'retweeted']
    print "Retweeted Status: ", d[u'retweeted_status']
    print "Source: ", d[u'source']
    print "Text: ", d[u'text']
    print "Truncated: ", d[u'truncated']
    print "User: ", d[u'user']         
                    
    break
connection.close()
