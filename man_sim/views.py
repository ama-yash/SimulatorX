from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render
from networkx import barabasi_albert_graph
from compartmental_models import si, sir, sis
import pandas as pd
import networkx as nx
from demographic_graph_generator import generate_nodes
def getIndex(request):
    template = "man_sim/index.html"
    data = pd.read_csv('datasets/demography.csv',index_col=0)

    area_names = list(data.index)
    data = {"dobj": area_names}
    return render(request, template, data)


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
    ethnicity = {
        "white": float(data["white"]),
        "black": float(data["black"]),
        "asian": float(data["asian"]),
        "other": float(data["other"]),
    }
    gender = {"male": float(data["male"]), "female": float(data["female"])}
    age = {
        "child": float(data["child"]),
        "adult": float(data["adult"]),
        "senior": float(data["senior"]),
    }


    is_sir = False
    model_name = None

    if int(data["graph_code"]) == 0:
        G = nx.empty_graph(N)
        is_activity_network = True
    elif int(data["graph_code"]) == 1:
        G = barabasi_albert_graph(N, 2)

    if model_type == 0:
        # SI model
        model_name = "SI"
        G = generate_nodes(G, ethnicity, gender, age)
        model_data = si(G, is_activity_network=is_activity_network, seeds=data["seeds"])
    elif model_type == 1:
        # SIS model
        model_name = "SIS"
        G = generate_nodes(G, ethnicity, gender, age)
        model_data = sis(G, is_activity_network=is_activity_network, seeds=data["seeds"])
        # model_data = simulate_sis(data)
    elif model_type == 2:
        # SIR model
        model_name = "SIR"
        G = generate_nodes(G, ethnicity, gender, age)
        model_data = sir(G, is_activity_network=is_activity_network, seeds=data["seeds"])
        is_sir = True

    data = {"data": model_data, "N": N, "model_name": model_name, "is_sir": is_sir, }

    return render(request, "includes/results/results_view.html", data)
