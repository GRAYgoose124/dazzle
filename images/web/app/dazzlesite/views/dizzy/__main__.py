import importlib
import os
from django.http import HttpResponse
import zmq
import json

# Dynamic import of dizzy_client.py - os.getenv("DIZZY_CLIENT_MODULE")?
# client = importlib.import_module("dizzy_client").client

from dizzy_client import dizzy_client as client


def request(request):
    test = client.request_workflow(
        request.GET.get("entity"), request.GET.get("workflow")
    )
    return HttpResponse(str(test))
