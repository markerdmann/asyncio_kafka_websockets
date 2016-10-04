import json
import random
import sys
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='10.57.111.175:9092')

from faker import Faker
f = Faker()

while True:

    blob = []
    for i in range(10):
        broker = {"name": f.name(), "avatar": "http://i.pravatar.cc/300"}
        blob.append(broker)

    msg = json.dumps(blob)
    print(msg)

    producer.send('elishatopic', msg.encode()).get(timeout=60)
    time.sleep(random.randint(1, 5))
