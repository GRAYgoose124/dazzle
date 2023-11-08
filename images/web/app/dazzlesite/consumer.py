from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

logger = logging.getLogger(__name__)


class FileWatcherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("file_watcher", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("file_watcher", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # Handle incoming messages if necessary

    async def file_changed(self, event):
        # Called when someone sends a message to the 'file_watcher' group
        logger.debug(f"Got message {event} at {self}")
        await self.send(text_data=json.dumps(event))
