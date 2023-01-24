import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async

class CartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'products'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        await self.close()

    async def product_save(self, event):
        await self.send(json.dumps(event['value']))

    async def product_delete(self, event):
        await self.send(str(event['value']))