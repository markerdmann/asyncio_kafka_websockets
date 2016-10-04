#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets
from kafka.common import KafkaError
from aiokafka import AIOKafkaConsumer
import time

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
    'foo', loop=loop, bootstrap_servers='localhost')

async def handler(websocket, path):
    while True:
        message = await consumer.getone()
        await websocket.send(message.value)

start_server = websockets.serve(handler, '127.0.0.1', 5678)

loop.run_until_complete(consumer.start())
loop.run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
