from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from semi_auto.models import Population

from .scripts.csv_generator_man import *
from .scripts.inf_predictor_manual import predict_infection
from .scripts.si_manual import *
from .scripts.sir_manual import *
from .scripts.sis_manual import *

# Create your views here.


def getIndex(request):
    template = "man_sim/index.html"
    area_names = Population.objects.raw(
        "select id,area_name from semi_auto_population;"
    )
    data = {"dobj": area_names}
    return render(request, template, data)


def getResult(request):
    N = int(request.POST.get("pop_size"))
    male = float(request.POST.get("male"))
    female = float(request.POST.get("female"))
    white = float(request.POST.get("white"))
    black = float(request.POST.get("black"))
    asian = float(request.POST.get("asian"))
    other = float(request.POST.get("other"))
    child = float(request.POST.get("child"))
    adult = float(request.POST.get("adult"))
    senior = float(request.POST.get("senior"))
    white_inf = float(request.POST.get("white_inf"))
    black_inf = float(request.POST.get("black_inf"))
    asian_inf = float(request.POST.get("asian_inf"))
    other_inf = float(request.POST.get("other_inf"))
    male_inf = float(request.POST.get("male_inf"))
    female_inf = float(request.POST.get("female_inf"))
    child_inf = float(request.POST.get("child_inf"))
    adult_inf = float(request.POST.get("adult_inf"))
    senior_inf = float(request.POST.get("senior_inf"))
    model_type = int(request.POST.get("model"))
    if model_type != 0:
        white_rec = float(request.POST.get("white_rec"))
        black_rec = float(request.POST.get("black_rec"))
        asian_rec = float(request.POST.get("asian_rec"))
        other_rec = float(request.POST.get("other_rec"))
        male_rec = float(request.POST.get("male_rec"))
        female_rec = float(request.POST.get("female_rec"))
        child_rec = float(request.POST.get("child_rec"))
        adult_rec = float(request.POST.get("adult_rec"))
        senior_rec = float(request.POST.get("senior_rec"))
    time = int(request.POST.get("time"))
    seeds = float(request.POST.get("seeds"))
    graph_type = int(request.POST.get("graph_type"))
    if graph_type == 1:
        m = int(request.POST.get("m"))
    else:
        m = 2
    population_parameters = {
        "N": N,
        "male": male,
        "female": female,
        "white": white,
        "black": black,
        "asian": asian,
        "other": other,
        "child": child,
        "adult": adult,
        "senior": senior,
    }
    if model_type == 0:
        disease_paramaters = {
            "white_inf": white_inf,
            "black_inf": black_inf,
            "asian_inf": asian_inf,
            "other_inf": other_inf,
            "male_inf": male_inf,
            "female_inf": female_inf,
            "child_inf": child_inf,
            "adult_inf": adult_inf,
            "senior_inf": senior_inf,
        }
    else:
        disease_paramaters = {
            "white_inf": white_inf,
            "black_inf": black_inf,
            "asian_inf": asian_inf,
            "other_inf": other_inf,
            "male_inf": male_inf,
            "female_inf": female_inf,
            "child_inf": child_inf,
            "adult_inf": adult_inf,
            "senior_inf": senior_inf,
            "white_rec": white_rec,
            "black_rec": black_rec,
            "asian_rec": asian_rec,
            "other_rec": other_rec,
            "male_rec": male_rec,
            "female_rec": female_rec,
            "child_rec": child_rec,
            "adult_rec": adult_rec,
            "senior_rec": senior_rec,
        }
    model_parameters = {"time": time, "seeds": seeds, "graph_type": graph_type, "m": m}
    if model_type == 0:
        data = simulate_si(population_parameters, disease_paramaters, model_parameters)
        template = "man_sim/si_result.html"
        filepath = "{}/log-man.csv".format(settings.MEDIA_ROOT)
        disease_paramaters["flag"] = model_parameters["graph_type"]
        disease_paramaters["m"] = model_parameters["m"]
        generate_CSV(population_parameters, disease_paramaters, filepath)
        data = {"data": data, "N": N}
        return render(request, template, data)
    elif model_type == 1:
        data = simulate_sis(population_parameters, disease_paramaters, model_parameters)
        filepath = "{}/log-man.csv".format(settings.MEDIA_ROOT)
        disease_paramaters["flag"] = model_parameters["graph_type"]
        disease_paramaters["m"] = model_parameters["m"]
        generate_CSV(population_parameters, disease_paramaters, filepath)
        template = "man_sim/sis_result.html"
        data = {"data": data, "N": N}
        return render(request, template, data)
    elif model_type == 2:
        data = simulate_sir(population_parameters, disease_paramaters, model_parameters)
        filepath = "{}/log-man.csv".format(settings.MEDIA_ROOT)
        disease_paramaters["flag"] = model_parameters["graph_type"]
        disease_paramaters["m"] = model_parameters["m"]
        generate_CSV(population_parameters, disease_paramaters, filepath)
        template = "man_sim/sir_result.html"
        data = {"data": data, "N": N}
        return render(request, template, data)


def predictInfection(request):
    n = int(request.POST.get("n"))
    gender = int(request.POST.get("gender"))
    ethnicity = int(request.POST.get("ethnicity"))
    age = int(request.POST.get("age"))
    parameters = {
        "N": n,
        "gender": gender,
        "ethnicity": ethnicity,
        "age": age,
        "filepath": "{}/log-man.csv".format(settings.MEDIA_ROOT),
    }
    prediction = predict_infection(parameters)
    data = {"pred": round(prediction, 2)}
    return JsonResponse(data)
