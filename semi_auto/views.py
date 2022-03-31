from tokenize import Number

import pandas as pd
from django.http.response import JsonResponse
from django.shortcuts import render


# Create your views here.
def getIndex(request):
    template = "semi_auto/index.html"
    data = pd.read_csv("datasets/demography.csv")

    area_names = list(data.index)
    data = {"dobj": area_names}
    return render(request, template, data)


def sendData(request):
    aid = request.POST.get("id")
    df = pd.read_csv("datasets/demography.csv", index_col=0)
    record = df.loc[aid]
    n = record["Males"] + record["Females"]

    # converting gender groups into ratios
    male_rat = round((record["Males"] / n) * 100, 2)
    female_rat = round((record["Females"] / n) * 100, 2)
    if male_rat + female_rat > 100:
        diff = (male_rat + female_rat) - 100
        female_rat = female_rat - diff
    elif male_rat + female_rat < 100:
        diff = 100 - (male_rat + female_rat)
        female_rat = female_rat + diff

    # converting ethnic groups into ratios
    white_rat = round((record["White"] / n) * 100, 2)
    black_rat = round((record["Black"] / n) * 100, 2)
    asian_rat = round((record["Asian"] / n) * 100, 2)
    other_rat = round((record["Other"] / n) * 100, 2)
    if white_rat + black_rat + asian_rat + other_rat > 100:
        diff = (white_rat + black_rat + asian_rat + other_rat) - 100
        other_rat = other_rat - diff
    elif white_rat + black_rat + asian_rat + other_rat < 100:
        diff = 100 - (white_rat + black_rat + asian_rat + other_rat)
        other_rat = other_rat + diff

    # converting age groups into ratios
    youth_rat = round((record["Youth"] / n) * 100, 2)
    adult_rat = round((record["Adult"] / n) * 100, 2)
    senior_rat = round((record["Senior"] / n) * 100, 2)
    if youth_rat + adult_rat + senior_rat > 100:
        diff = (youth_rat + adult_rat + senior_rat) - 100
        senior_rat = senior_rat - diff
    elif youth_rat + adult_rat + senior_rat < 100:
        diff = 100 - (youth_rat + adult_rat + senior_rat)
        senior_rat = senior_rat + diff

    # packing and sending data
    data = {
        "population": int(n),
        "white": float(white_rat),
        "black": float(black_rat),
        "asian": float(asian_rat),
        "other": round(float(other_rat), 2),
        "male": float(male_rat),
        "female": round(float(female_rat), 2),
        "child": float(youth_rat),
        "adult": float(adult_rat),
        "senior": round(float(senior_rat), 2),
    }
    return JsonResponse(data)
