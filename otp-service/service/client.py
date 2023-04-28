import asyncio
import websockets
import json


async def PingServer():

    URL='ws://127.0.0.1:8080/ws/cluster/'
    async with websockets.connect(URL) as ws:
        res=await ws.recv()
        print(json.loads(res))


loop = asyncio.get_event_loop()
task = loop.create_task(PingServer)
loop.run_forever()

