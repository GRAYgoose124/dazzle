from django.shortcuts import render
from dizzy_client import dizzy_client as client


default_dict_data = {
    "entity": "einz",
    "workflow": "einzy",
    "service": "status",
    "task": "Info",
}


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
