from django.http.response import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .scripts.sis_covid import *
from .scripts.csv_generator import *
from .scripts.infection_prediction import *
from .scripts.sir_covid import *
from .scripts.si_covid import *
from semi_auto.models import Population
# Create your views here.
def getIndex(request):
    template = 'covid19/index.html'
    area_names = Population.objects.raw('select id,area_name from semi_auto_population;')
    data = {'dobj':area_names}
    return render(request,template,data)

def getResult(request):
    N = int(request.POST.get('pop_size'))
    male = float(request.POST.get('male'))
    female = float(request.POST.get('female'))
    white = float(request.POST.get('white'))
    black = float(request.POST.get('black'))
    asian = float(request.POST.get('asian'))
    other = float(request.POST.get('other'))
    child = float(request.POST.get('child'))
    adult = float(request.POST.get('adult'))
    senior = float(request.POST.get('senior'))
    model_type = int(request.POST.get('model'))
    time = int(request.POST.get('time'))
    seeds = float(request.POST.get('seeds'))
    parameters = {
        'N':N,
        'male':male,
        'female':female,
        'white':white,
        'black':black,
        'asian':asian,
        'other':other,
        'child':child,
        'adult':adult,
        'senior':senior,
        'time':time,
        'seeds':seeds    
    }
    if model_type == 0:
        si_data = simulate_si(parameters)
        filepath = '{}/log.csv'.format(settings.MEDIA_ROOT)
        generate_CSV(parameters,filepath)
        data = {'data':si_data,'N':N}
        template = 'covid19/si_result.html'
        return render(request,template,data)
    elif model_type == 1: 
        sis_data = simulate_sis(parameters)
        filepath = '{}/log.csv'.format(settings.MEDIA_ROOT)
        generate_CSV(parameters,filepath)
        data = {'data':sis_data,'N':N}
        template = 'covid19/sis_result.html'
        return render(request,template,data)
    elif model_type == 2:
        sir_data = simulate_sir(parameters)
        filepath = '{}/log.csv'.format(settings.MEDIA_ROOT)
        generate_CSV(parameters,filepath)
        data = {'data':sir_data,'N':N}
        template = 'covid19/sir_result.html'
        return render(request,template,data)

def predictInfection(request):
    n = int(request.POST.get('n'))
    gender = int(request.POST.get('gender'))
    ethnicity = int(request.POST.get('ethnicity'))
    age = int(request.POST.get('age'))
    age2 = int(request.POST.get('age2'))
    parameters = {
        'N':n,
        'gender':gender,
        'ethnicity':ethnicity,
        'target_age':age,
        'source_age':age2,
        'filepath': '{}/log.csv'.format(settings.MEDIA_ROOT)
    }
    prediction = predict_infection(parameters)
    data = {'pred':round(prediction,2)}
    return JsonResponse(data)