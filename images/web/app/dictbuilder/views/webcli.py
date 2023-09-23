from django.shortcuts import render


def webcli(request):
    return render(request, "webcli.html")
