#!/usr/bin/env python

import asyncio
import websockets
from aiokafka import AIOKafkaConsumer

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
    'mytopic', loop=loop, bootstrap_servers='localhost')

async def handler(websocket, path):
    while True:
        message = await consumer.getone()
        await websocket.send(message.value.decode())

start_server = websockets.serve(handler, '127.0.0.1', 5678)

loop.run_until_complete(consumer.start())
loop.run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
