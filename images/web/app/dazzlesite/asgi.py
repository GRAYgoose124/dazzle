"""
ASGI config for dazzlesite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os, asyncio, logging

from django.core.asgi import get_asgi_application
from .wf_handlers import file_change_handler


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dazzlesite.settings")


application = get_asgi_application()


# Start the watchfiles coroutine
paths = ["/data/shared/projects/"]
loop = asyncio.get_event_loop()
loop.create_task(file_change_handler(paths))
