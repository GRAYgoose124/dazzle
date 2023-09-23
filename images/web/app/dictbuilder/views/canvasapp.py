from django.shortcuts import render


def canvasapp(request):
    return render(request, "canvasapp.html")
