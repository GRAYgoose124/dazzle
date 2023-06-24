from django.shortcuts import render

from dizzy_client import dizzy_client as client

# Example data
dict_data = {"entity": None, "workflow": None}


def dict_builder(request):
    dict_data["entity"] = request.GET.get("entity") or dict_data["entity"]
    dict_data["workflow"] = request.GET.get("workflow") or dict_data["workflow"]

    if request.method == "POST":
        # Get the updated values from the form
        for key in dict_data:
            dict_data[key] = request.POST.get(key, "")

    if request.method == "GET" or "Submit" in request.POST:
        response = client.request_workflow(dict_data["entity"], dict_data["workflow"])
    else:
        response = "Updated!"

    return render(
        request,
        "dict_builder.html",
        {"dict_data": dict_data, "dizzy": response},
    )
