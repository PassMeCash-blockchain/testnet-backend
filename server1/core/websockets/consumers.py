from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.exceptions import StopConsumer


class WebsocketCluster(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['layer_id']
        self.room_group_name='instance-' + self.room_name
        await self.accept()
        await self.send(text_data=json.dumps(
            {"connected":"connected to server instance"}
        ))
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            recieved_data=json.loads(text_data)
            message=recieved_data['message']
            sender=recieved_data['sender']
            if message['success']=='otp sent' and sender=='otp-service':
                await self.send(
                text_data=json.dumps(
                    {
                    'confirmed':'confirmed sent'
                }
                )
            )
            # ------------------------Uncomment this code and break the prod Server :)---------------------
            # await self.channel_layer.group_send(
            #     self.room_group_name,
            #     {
            #     'type':'chat_message',
            #     'message':message,
            #     'sender':sender,
            #     }
            #     )

    async def chat_message(self,event):
        message=event['message']
        sender=event['sender']
        await self.send(text_data=json.dumps({
            'message':message,
            'sender':sender,
        }))
    async def disconnect(self, code):
        print('disconnected')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
