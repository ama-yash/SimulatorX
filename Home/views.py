from django.shortcuts import render


def getIndex(request):
    template = "index.html"
    data = {}
    return render(request, template, data)
