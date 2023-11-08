from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import FileWatcherConsumer

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(
            [
                path("ws/file_watcher/", FileWatcherConsumer.as_asgi()),
            ]
        ),
    }
)
