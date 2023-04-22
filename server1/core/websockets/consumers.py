from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.exceptions import StopConsumer


class WebsocketCluster(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name='cluster'
        self.room_group_name='instance ' + self.room_name
        await self.accept()
        await self.send(text_data='connected')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        pass
    async def chat_message(self,event):
        pass
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
