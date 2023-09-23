from django.http import JsonResponse
from django.shortcuts import render


def schedule(request):
    if request.method == "POST":
        job_name = request.POST.get("jobName")
        queue = request.POST.getlist("queue[]")
        # Process the submitted queue data
        # ...

        # Return a JSON response
        return JsonResponse({"message": "Queue submitted successfully."})

    return render(request, "schedule.html")
