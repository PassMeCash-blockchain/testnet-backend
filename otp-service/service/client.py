import asyncio
import websockets
import json


async def PingServer(payload,layer_id):

    URL=f'ws://127.0.0.1:8080/ws/cluster/{layer_id}/'
    async with websockets.connect(URL) as ws:
        await ws.send(payload)
        while True:
            res=await ws.recv()
            res_conv=json.loads(res)
            print(res_conv)
            try:
                if res_conv['confirmed']:
                    break
            except:
                print("otp not confirmed")


# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(asyncio.gather(PingServer()))

async def main():
    await PingServer(payload='')

if __name__ == "__main__":
    asyncio.run(main())

