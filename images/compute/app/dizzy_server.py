import os
import sys
from dizzy.daemon import Server
import logging
import asyncio

logging.basicConfig(level=getattr(logging, os.getenv("DIZZY_LOG_LEVEL", "INFO")))


server = Server(port=os.getenv("DIZZY_COMPUTE_PORT"))
asyncio.run(server.run())
