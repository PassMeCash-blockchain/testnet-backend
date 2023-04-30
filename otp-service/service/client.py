import asyncio
import websockets
import json


async def PingServer(payload):

    URL='ws://127.0.0.1:8080/ws/cluster/'
    async with websockets.connect(URL) as ws:
        while True:
            await ws.send(payload)
            res=await ws.recv()
            print(res)
            break


# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(asyncio.gather(PingServer()))

async def main():
    await PingServer(payload='')

if __name__ == "__main__":
    asyncio.run(main())

