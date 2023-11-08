import asyncio, logging

from watchfiles import awatch
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


log = logging.getLogger(__name__)


async def file_change_handler(paths):
    log.info(f"Watching {paths}")
    async for changes in awatch(paths):
        for change in changes:
            change_type, path = change
            async_to_sync(get_channel_layer().group_send)(
                "file_watcher",
                {
                    "type": "file.changed",
                    "message": {
                        "event_type": change_type.name,  # CREATED, MODIFIED, DELETED
                        "path": str(path),
                    },
                },
            )
