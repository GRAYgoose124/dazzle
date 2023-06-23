import os
import sys
from dizzy.daemon import Server


server = Server(port=os.getenv("DIZZY_COMPUTE_PORT"))
server.run()
