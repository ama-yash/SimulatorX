from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from semi_auto.models import Population
from .scripts.csv_generator import *
from .scripts.infection_prediction import *
from compartmental_models import Models

def getIndex(request):
    area_names = Population.objects.raw(
        "select id,area_name from semi_auto_population;"
    )
    data = {"dobj": area_names}
    return render(request, "covid19/index.html", data)


def getResult(request):

    if request.POST:
        data = dict(request.POST.items())
        # remove csrf token here, altough we should use it to verify the request is legitemate and not for example a bot or DDOS
        del data["csrfmiddlewaretoken"]

    N = 0
    model_type = 0
    if data:
        N = int(data.get("pop_size"))
        model_type = int(data.get("model"))
    data["graph_code"] = 0
    data["m"] = 2
    filepath = "{}/log.csv".format(settings.MEDIA_ROOT)
    generate_CSV(data, filepath)
    if model_type == 0:
        # SI model
        #model_data = simulate_si(data)
        model = Models(mode='covid',parameters=data)
        model_data = model.si()
        template = "covid19/si_result.html"
    elif model_type == 1:
        # SIS model
        #model_data = simulate_sis(data)
        model = Models(mode='covid',parameters=data)
        model_data = model.sis()
        template = "covid19/sis_result.html"
    elif model_type == 2:
        # SIR model
        #model_data = simulate_sir(data)
        model = Models(mode='covid',parameters=data)
        model_data = model.sir()
        template = "covid19/sir_result.html"

    data = {"data": model_data, "N": N}

    return render(request, template, data)


def predictInfection(request):

    if request.POST:
        data = dict(request.POST.items())
        # remove csrf token here, altough we should use it to verify the request is legitemate and not for example a bot or DDOS
        del data["csrfmiddlewaretoken"]

    parameters = {
        "N": data.get("n"),
        "gender": data.get("gender"),
        "ethnicity": data.get("ethnicity"),
        "target_age": data.get("age"),
        "source_age": data.get("age2"),
        "filepath": "{}/log.csv".format(settings.MEDIA_ROOT),
    }
    prediction = predict_infection(parameters)

    data = {"pred": round(prediction, 2)}

    return JsonResponse(data)
