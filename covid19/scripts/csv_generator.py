import pandas as pd
import random
import numpy as np
import networkx as nx
from genNode import generateNodes
from cov19_simulation_tools import get_beta,loadDep

def generate_DataFrame():
    dff_test = pd.DataFrame(columns=['Ethnicity','Gender','Target_Age','Source_Age','Beta_Class'])
    return dff_test

def run(G,N,dataframe):
    dff_test = generate_DataFrame()
    eth = []
    gen = []
    age = []
    age2 = []
    beta = []
    for n in range(0,N):
        cont = int(random.randint(0,N-1))
        temp_age = G.nodes[cont]['age']
        b = get_beta(n,cont,G,dataframe)
        if b >= 0 and b <= 0.01:
            b = 0
        elif b > 0.01 and b <= 0.02:
            b = 1
        elif b > 0.02 and b <= 0.03:
            b = 2
        elif b > 0.03 and b <= 0.04:
            b = 3
        elif b > 0.04 and b <= 0.05:
            b = 4
        elif b > 0.05 and b <= 0.06:
            b = 5
        elif b > 0.06 and b <= 0.07:
            b = 6
        elif b > 0.07 and b <= 0.08:
            b = 7
        elif b > 0.08 and b <= 0.09:
            b = 8
        elif b > 0.09 and b <= 0.1:
            b = 9
        elif b > 0.1 and b <= 0.11:
            b = 10
        elif b > 0.11 and b <= 0.12:
            b = 11
        elif b > 0.12 and b <= 0.13:
            b = 12
        elif b > 0.13 and b <= 0.14:
            b = 13
        elif b > 0.14 and b <= 0.15:
            b = 14
        elif b > 0.15 and b <= 0.16:
            b = 15
        elif b > 0.16 and b <= 0.17:
            b = 16
        elif b > 0.17 and b <= 0.18:
            b = 17
        elif b > 0.18 and b <= 0.19:
            b = 18
        elif b > 0.19 and b < 0.2:
            b = 19
        eth.append(G.nodes[n]['ethnicity'])
        gen.append(G.nodes[n]['gender'])
        age.append(G.nodes[n]['age'])
        age2.append(temp_age)
        beta.append(b)
    dff_test['Ethnicity'] = eth
    dff_test['Gender'] = gen
    dff_test['Target_Age'] = age
    dff_test['Source_Age'] = age2
    dff_test['Beta_Class'] = beta
    return dff_test
def generate_CSV(parameters,filepath):
    N = parameters['N']
    data = loadDep()
    ethn = {'white':parameters['white'],'black':parameters['black'],'asian':parameters['asian'],'other':parameters['other']}
    gen = {'male':parameters['male'],'female':parameters['female']}
    ag = {'child':parameters['child'],'adult':parameters['adult'],'senior':parameters['senior']}
    graph = {
        'code':1,
        'm':2
    }
    G = generateNodes(N,ethn,gen,ag,graph)
    dframe = run(G,N,data)
    dframe = dframe[['Ethnicity','Gender','Target_Age','Source_Age','Beta_Class']]
    dframe.to_csv(filepath,index=False)