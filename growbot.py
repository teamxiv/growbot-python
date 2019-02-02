import websockets
import json
import asyncio

class UnhandledRPCTranslationException(Exception):
    pass

class Robot(object):
    def __init__(self, id, host="ws://api.growbot.tardis.ed.ac.uk"):
        self.id = id
        self.host = host
        self.callbacks = {}

    async def connect(self):
        self.ws = await websockets.connect(self.host+"/stream/"+self.id)
        async for message in self.ws:
            result = json.loads(message)

            type = result['type']
            data = result['data']
            if type in self.callbacks:
                self._translate_call(type, data, self.callbacks[type])
            else:
                print("Uncaught message for type", type, "with data", data)

    def close(self):
        self.ws.close()

    def add_callback(self, type, fn):
        self.callbacks[type] = fn

    """
    Internal only
    """
    def _translate_call(self, type, data, fn):
        if type == "move":
            fn(data)
        else:
            raise UnhandledRPCTranslationException()
