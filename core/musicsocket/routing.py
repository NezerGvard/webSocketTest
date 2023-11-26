from django.urls import path
from . import  consumers

websocket_urlpatterns = [
    path(r'ws', consumers.MusicConsumer.as_asgi()),
    path(r'', consumers.MusicConsumer.as_asgi()),
]