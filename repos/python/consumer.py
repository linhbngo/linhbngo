import sys
import logging

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

logging.basicConfig(
  format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
  level=logging.DEBUG
)


#kafka = KafkaClient(sys.argv[1] + ":9092")
# On Clemson Hadoop cluster, we use the Hortonworks port for Kafka: 6667
kafka = KafkaClient(sys.argv[1] + ":6667")

print("After connecting to kafka")

consumer = SimpleConsumer(kafka, "my-group", sys.argv[2])

for message in consumer:
    print(message)

