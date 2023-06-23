import os
from django.http import HttpResponse
import zmq
import json


class DizzyClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Singleton"""
        if cls._instance is None:
            cls._instance = super(DizzyClient, cls).__new__(cls)

        return cls._instance

    def __init__(self, address="localhost", port=5555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{address}:{port}")

    def request_workflow(self, entity: str = "einz", workflow: str = "einzy"):
        self.socket.send_json({"entity": entity, "workflow": workflow})
        return json.loads(self.socket.recv().decode())


client = DizzyClient(
    address=os.getenv("DIZZY_COMPUTE_HOST"),
    port=os.getenv("DIZZY_COMPUTE_PORT"),
)


def request(request):
    test = client.request_workflow(
        request.GET.get("entity"), request.GET.get("workflow")
    )
    return HttpResponse(str(test))
