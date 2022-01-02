import pandas as pd
import random
import numpy as np
from count import count_all_si
import networkx as nx
from genNode import generateNodes
from gen_simulation_tools import infect,recover_sis,seed_graph

def power_law(x0, x1, gamma,N):
    pl = []
    for i in range (N):
        pl.append(((x1**(gamma+1) - x0**(gamma+1))*random.uniform(0,1)  + x0**(gamma+1.0))**(1.0/(gamma + 1.0)))
    return pl

def activate_graph(activity, graph,N):
    active_nodes = []
    for i in range(N):
        if (random.random() < activity[i]):
            active_nodes.append(i)
    return active_nodes

def simulate_sis(population_parameters,disease_parameters,model_parameters):
    N = population_parameters['N']
    ethn = {'white':population_parameters['white'],'black':population_parameters['black'],'asian':population_parameters['asian'],'other':population_parameters['other']}
    gen = {'male':population_parameters['male'],'female':population_parameters['female']}
    ag = {'child':population_parameters['child'],'adult':population_parameters['adult'],'senior':population_parameters['senior']}
    infection_parameters = {'white':disease_parameters['white_inf'],
                            'black':disease_parameters['black_inf'],
                            'asian':disease_parameters['asian_inf'],
                            'other':disease_parameters['other_inf'],
                            'male':disease_parameters['male_inf'],
                            'female':disease_parameters['female_inf'],
                            'child':disease_parameters['child_inf'],
                            'adult':disease_parameters['adult_inf'],
                            'senior':disease_parameters['senior_inf'],
                          }
    recovery_parameters = {'white':disease_parameters['white_rec'],
                            'black':disease_parameters['black_rec'],
                            'asian':disease_parameters['asian_rec'],
                            'other':disease_parameters['other_rec'],
                            'male':disease_parameters['male_rec'],
                            'female':disease_parameters['female_rec'],
                            'child':disease_parameters['child_rec'],
                            'adult':disease_parameters['adult_rec'],
                            'senior':disease_parameters['senior_rec'],
                          }                      
    g_type = model_parameters['graph_type']
    if g_type == 0:
        graph = {
            'code': g_type,
        }
        m = 2
    elif g_type == 1:
        graph = {
            'code': g_type,
            'm': model_parameters['m']
        }
        m = model_parameters['m']
    G = generateNodes(N,ethn,gen,ag,graph)
    epsilon = 0.001
    eta = 1.
    gamma = -2.1
    act = power_law(epsilon,1,gamma,N)
    infected_population = []
    susceptible_population = []
    white_sus_pop = []
    white_inf_pop = []
    black_sus_pop = []
    black_inf_pop = []
    asian_sus_pop = []
    asian_inf_pop = []
    other_sus_pop = []
    other_inf_pop = []
    male_inf_pop = []
    male_sus_pop = []
    female_inf_pop = []
    female_sus_pop = []
    child_inf_pop = []
    child_sus_pop = []
    adult_inf_pop = []
    adult_sus_pop = []
    senior_inf_pop = []
    senior_sus_pop = []
    seeds = int(model_parameters['seeds'])
    seed_graph(G,seeds)
    for i in range(model_parameters['time']):
        if g_type == 0:
            active_nodes = activate_graph(act,G,N)
            for i in active_nodes:
              count=0
              while count<m:
                  target=random.randint(0,N-1)
                  if target!=i and target not in G.neighbors(i):
                      G.add_edge(i,target)
                      count+=1
        else:
            active_nodes = G.nodes()
        infect(active_nodes,G,infection_parameters)
        recover_sis(active_nodes,G,recovery_parameters)
        data = count_all_si(G)
        susceptible_population.append(data['total_sus'])
        infected_population.append(data['total_inf'])
        white_sus_pop.append(data['white_sus'])
        white_inf_pop.append(data['white_inf'])
        black_sus_pop.append(data['black_sus'])
        black_inf_pop.append(data['black_inf'])
        asian_sus_pop.append(data['asian_sus'])
        asian_inf_pop.append(data['asian_inf'])
        other_sus_pop.append(data['other_sus'])
        other_inf_pop.append(data['other_inf'])
        male_sus_pop.append(data['male_sus'])
        male_inf_pop.append(data['male_inf'])
        female_sus_pop.append(data['female_sus'])
        female_inf_pop.append(data['female_inf'])
        child_sus_pop.append(data['child_sus'])
        child_inf_pop.append(data['child_inf'])
        adult_sus_pop.append(data['adult_sus'])
        adult_inf_pop.append(data['adult_inf'])
        senior_sus_pop.append(data['senior_sus'])
        senior_inf_pop.append(data['senior_inf'])
    data = {
        'sus_total':susceptible_population,
        'inf_total':infected_population,
        'white_sus':white_sus_pop,
        'white_inf':white_inf_pop,
        'black_sus':black_sus_pop,
        'black_inf':black_inf_pop,
        'asian_sus':asian_sus_pop,
        'asian_inf':asian_inf_pop,
        'other_sus':other_sus_pop,
        'other_inf':other_inf_pop,
        'male_inf':male_inf_pop,
        'male_sus':male_sus_pop,
        'female_inf':female_inf_pop,
        'female_sus':female_sus_pop,
        'child_inf':child_inf_pop,
        'child_sus':child_sus_pop,
        'adult_inf':adult_inf_pop,
        'adult_sus':adult_sus_pop,
        'senior_inf':senior_inf_pop,
        'senior_sus':senior_sus_pop
    }       
    return data

population_parameters = {
        'N':2000,
        'male':50.6,
        'female':49.4,
        'white':62.5,
        'black':19.1,
        'asian':11.7,
        'other':6.7,
        'child':20,
        'adult':60,
        'senior':20, 
    }
disease_parameters = {
        'white_inf':0.15,
        'black_inf':0.15,
        'asian_inf':0.15,
        'other_inf':0.15,
        'male_inf':0.15,
        'female_inf':0.15,
        'child_inf':0.15,
        'adult_inf':0.15,
        'senior_inf':0.15,
        'white_rec':0.05,
        'black_rec':0.05,
        'asian_rec':0.05,
        'other_rec':0.05,
        'male_rec':0.05,
        'female_rec':0.05,
        'child_rec':0.05,
        'adult_rec':0.05,
        'senior_rec':0.05,
}
model_parameters = {
        'graph_type':1,
        'time':100,
        'seeds':25,
        'm':2
}

