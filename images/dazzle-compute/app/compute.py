import sys
from dizzy.daemon import Server


server = Server(port=5555)
server.run()
