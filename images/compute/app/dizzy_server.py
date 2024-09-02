import os
import sys
import logging
import asyncio

from dizzy.daemon import Server
from dizzy.utils import load_dizzy_proto_class

logging.basicConfig(level=getattr(logging, os.getenv("DIZZY_LOG_LEVEL", "INFO")), filename="/app/dizzy_server.log")


DizzyProtocol = load_dizzy_proto_class()

server = Server(DizzyProtocol, port=os.getenv("DIZZY_COMPUTE_PORT"))
asyncio.run(server.run())
