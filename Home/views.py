from django.shortcuts import render

# Create your views here.

def getIndex(request):
    template = 'index.html'
    data = {}
    return render(request,template,data)