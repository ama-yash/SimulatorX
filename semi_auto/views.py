from django.http.response import JsonResponse
from django.shortcuts import render

from .models import Population


# Create your views here.
def getIndex(request):
    template = "semi_auto/index.html"
    area_names = Population.objects.raw(
        "select id,area_name from semi_auto_population;"
    )
    data = {"dobj": area_names}
    return render(request, template, data)


def sendData(request):
    aid = int(request.POST.get("id"))
    obj = Population.objects.raw(
        "select * from semi_auto_population where id = {};".format(aid)
    )
    data = {
        "population": obj[0].population,
        "white": obj[0].white,
        "black": obj[0].black,
        "asian": obj[0].asian,
        "other": obj[0].other,
        "male": obj[0].male,
        "female": obj[0].female,
        "child": obj[0].child,
        "adult": obj[0].adult,
        "senior": obj[0].senior,
    }
    return JsonResponse(data)
