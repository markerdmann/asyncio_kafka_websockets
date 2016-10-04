#!/usr/bin/env python

import asyncio
import sys
import websockets
from aiokafka import AIOKafkaConsumer

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
    sys.argv[1], loop=loop, bootstrap_servers='10.57.111.175:9092')

connected = set()

async def handler(websocket, path):
    global connected
    connected.add(websocket)
    try:
        while True:
            message = await consumer.getone()
            val = message.value.decode()
            print(val)
            await asyncio.wait([ws.send(val) for ws in connected])
    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, 'localhost', 5678)

loop.run_until_complete(consumer.start())
loop.run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
