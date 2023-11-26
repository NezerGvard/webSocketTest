from channels.consumer import AsyncConsumer
from core.settings import MEDIA_ROOT
import os


class MusicConsumer(AsyncConsumer):

    channel_layer_alias = "echo_alias"

    async def websocket_connect(self, event):
        print(event, 11111111111)
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        print(text_data, "dadadadadadadadadadadadadadadad")
        print(MEDIA_ROOT+'\sample-15s.wav')
        file_path = os.path.join(MEDIA_ROOT+'\sample-15s.wav')

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                audio_data = file.read()

                await self.send({
                    "type": "websocket.send",
                    "bytes": audio_data,
                })
        else:
            await self.send({
                "type": "websocket.send",
                "text": "File not found",
            })


    async def websocket_disconnect(self, event):
        pass