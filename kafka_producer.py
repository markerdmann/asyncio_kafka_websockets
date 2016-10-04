import sys

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost')

try:
    num_messages = int(sys.argv[1])
except (IndexError, ValueError):
    num_messages = 1000

for i in range(num_messages):
    msg = 'Hello World {}'.format(i)
    producer.send('mytopic', msg.encode()).get(timeout=60)
