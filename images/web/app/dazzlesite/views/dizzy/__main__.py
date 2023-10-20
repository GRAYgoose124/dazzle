import importlib
import os
from django.http import HttpResponse, JsonResponse
import zmq
import json

# Dynamic import of dizzy_client.py - os.getenv("DIZZY_CLIENT_MODULE")?
# client = importlib.import_module("dizzy_client").client

from dizzy_client import dizzy_client as client


async def request(request):
    try:
        dizzy_req = {"entity": "", "workflow": ""}
        if request.method == "GET":
            if "entity" in request.GET:
                dizzy_req["entity"] = request.GET.get("entity")

            if "workflow" in request.GET:
                dizzy_req["workflow"] = request.GET.get("workflow")

        test = await client.send_request(dizzy_req)
    except Exception as e:
        return JsonResponse({"error": str(e)})
    return JsonResponse({"test": test})
