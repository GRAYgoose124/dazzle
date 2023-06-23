from django.http import HttpResponse
import zmq
import json


class DizzyClient:
    def __init__(self, address="localhost", port=5555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{address}:{port}")

    def request_workflow(self, entity: str = "einz", workflow: str = "einzy"):
        self.socket.send_json({"entity": entity, "workflow": workflow})
        return json.loads(self.socket.recv().decode())


client = DizzyClient(address="dazzle-compute", port=5555)


def request(request):
    test = client.request_workflow()
    return HttpResponse(str(test))
