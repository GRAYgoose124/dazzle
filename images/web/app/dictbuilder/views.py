import json
from django.shortcuts import render
from dizzy_client import dizzy_client as client
from django.http import JsonResponse
from django.views import View
import inspect

default_dict_data = {
    "entity": "einz",
    "workflow": "einzy",
    "service": "status",
    "task": "Info",
}


def canvasapp(request):
    return render(request, "canvasapp.html")


def dictbuilder(request):
    dict_data = {
        "entity": "",
        "workflow": "",
        "service": "",
        "task": "",
    }

    response = {}
    if request.method == "GET":
        if "entity" in request.GET:
            dict_data["entity"] = request.GET.get("entity") or dict_data["entity"]
        else:
            del dict_data["entity"]

        if "workflow" in request.GET:
            dict_data["workflow"] = request.GET.get("workflow") or dict_data["workflow"]
        else:
            del dict_data["workflow"]

        if "service" in request.GET:
            dict_data["service"] = request.GET.get("service") or dict_data["service"]
        else:
            del dict_data["service"]

        if "task" in request.GET:
            dict_data["task"] = request.GET.get("task") or dict_data["task"]
        else:
            del dict_data["task"]

    elif request.method == "POST":
        if "ChangeKeys" in request.POST:
            selected_keys = request.POST.get("ChangeKeys", "").split("_")
            dict_data = {
                key: value
                for key, value in default_dict_data.items()
                if key in selected_keys
            }

        for key in dict_data:
            if key in request.POST and request.POST.get(key) != "":
                dict_data[key] = request.POST.get(key)

        # remove empty keys
        dict_data = {key: value for key, value in dict_data.items() if value != ""}

        if "Submit" in request.POST:
            if "entity" in dict_data and "workflow" in dict_data:
                response = client.request_workflow(
                    dict_data["entity"], dict_data["workflow"]
                )

            if "service" in dict_data and "task" in dict_data:
                response = client.request_task(dict_data["service"], dict_data["task"])

    return render(
        request,
        "dictbuilder.html",
        {"dict_data": dict_data, "dizzy": response},
    )


def webcli(request):
    return render(request, "webcli.html")


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


def schedule(request):
    if request.method == "POST":
        job_name = request.POST.get("jobName")
        queue = request.POST.getlist("queue[]")
        # Process the submitted queue data
        # ...

        # Return a JSON response
        return JsonResponse({"message": "Queue submitted successfully."})

    return render(request, "schedule.html")


class DynamicArgsView(View):
    def get(self, request, *args, **kwargs):
        function_namespace = kwargs.get("function_namespace", None)

        # Split the namespace by dots
        modules = function_namespace.split(".")

        # Import the module
        module = __import__(modules[0])

        for mod in modules[1:-1]:
            module = getattr(module, mod)

        func_name = modules[-1]

        # Get the function from the module
        function = getattr(module, func_name)

        # Get the function arguments
        argspec = inspect.getfullargspec(function)

        # # Prepare the arguments from the request
        # func_args = {
        #     arg: request.GET.get(arg, None) for arg in argspec.args if arg != "self"
        # }

        # Call the function with the prepared arguments
        # response = function(**func_args)

        return JsonResponse({"response": argspec.args})
