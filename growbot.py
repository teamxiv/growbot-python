import websockets
import asyncio

class Robot(object):
    def __init__(self, id, host="ws://api.growbot.tardis.ed.ac.uk"):
        self.id = id
        self.host = host

    async def connect(self):
        self.ws = await websockets.connect(self.host+"/stream/"+self.id)
        async for message in self.ws:
            print(message)

    def close(self):
        self.ws.close()
