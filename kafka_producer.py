import json
import random
import sys
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost')

try:
    num_messages = int(sys.argv[1])
except (IndexError, ValueError):
    num_messages = 1000

product_list = """Office
    Industrial
    Retail
    Land
    Multi-family
    Hotel
    Other"""
product_list = [x.lower() for x in product_list.split('\n')]


while True:

    blob = {
    	"latitude": random.randint(18, 48),
        "longitude": random.randint(-125, -62),
        "revenue": random.randint(0, 1000000000),
    	"magnitude": random.randint(0, 10),
    	"brokers": [
    		{"name": "Jon Snow", "avatar": "http://i.pravatar.cc/300"}
    	],
    	"product": random.choice(product_list)}

    msg = json.dumps(blob)
    print(msg)

    producer.send('mytopic', msg.encode()).get(timeout=60)
    time.sleep(random.random())
