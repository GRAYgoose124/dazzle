import os
import sys
from dizzy.daemon import Server
import logging

logging.basicConfig(level=logging.DEBUG)


server = Server(port=os.getenv("DIZZY_COMPUTE_PORT"))
server.run()
