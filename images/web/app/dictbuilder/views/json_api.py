import json
from django.http import JsonResponse

from dizzy_client import dizzy_client as client


def json_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        command = data.get("command", "")

        response_data = {"result": None}
        match command.split():
            case ["request", "workflow", entity, workflow]:
                response_data["result"] = client.request_workflow(entity, workflow)
            case ["request", "task", service, task]:
                response_data["result"] = client.request_task(service, task)
            case _:
                response_data["result"] = f"Invalid command {command}"
        # response_data = {"message": "Command received and processed successfully"}

        return JsonResponse(response_data)

    # Handle other HTTP methods if necessary
    return JsonResponse({"result": "Invalid request"})
