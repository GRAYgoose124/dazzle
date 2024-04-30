import os
import asyncio
import logging
from django.core.asgi import get_asgi_application
from .wf_handlers import file_change_handler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dazzlesite.settings")
django_asgi_app = get_asgi_application()
logger = logging.getLogger("dazzlesite")


async def application(scope, receive, send):
    if scope["type"] == "lifespan":
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                logger.info("Starting up...")
                paths = ["/data/shared/projects/"]
                loop = asyncio.get_event_loop()
                loop.create_task(file_change_handler(paths))
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                logger.info("Shutting down...")
                await send({"type": "lifespan.shutdown.complete"})
                break
    else:
        await django_asgi_app(scope, receive, send)
