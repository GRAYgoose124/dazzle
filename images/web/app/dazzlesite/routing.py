import logging

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import FileWatcherConsumer

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.debug("Starting routing.py")

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(
            [
                path("ws/file_watcher/", FileWatcherConsumer.as_asgi()),
            ]
        ),
    }
)
