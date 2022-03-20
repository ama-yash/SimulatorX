from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render

from semi_auto.models import Population


def getIndex(request):
    area_names = Population.objects.raw(
        "select id,area_name from semi_auto_population;"
    )
    data = {"dobj": area_names}
    return render(request, "man_sim/index.html", data)


def getResult(request):

    if request.POST:
        data = dict(request.POST.items())
        # remove csrf token here, altough we should use it to verify the request is legitemate and not for example a bot or DDOS
        del data["csrfmiddlewaretoken"]
    if data["m"] == "":
        data["m"] = 2
    N = 0
    model_type = 0
    if data:
        N = int(data.get("pop_size"))
        model_type = int(data.get("model"))
    if model_type == 0:
        # SI model
        model = Models(mode="manual", parameters=data)
        model_data = model.si()
        # model_data = simulate_si(data)
        template = "man_sim/si_result.html"
    elif model_type == 1:
        # SIS model
        model = Models(mode="manual", parameters=data)
        model_data = model.sis()
        # model_data = simulate_sis(data)
        template = "man_sim/sis_result.html"
    elif model_type == 2:
        # SIR model
        # model_data = simulate_sir(data)
        model = Models(mode="manual", parameters=data)
        model_data = model.sir()
        template = "man_sim/sir_result.html"

    data = {"data": model_data, "N": N}

    return render(request, template, data)
