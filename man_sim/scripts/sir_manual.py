import random
import numpy as np
import networkx as nx
from genNode import generateNodes
from count import count_all_sir
from gen_simulation_tools import infect,recover_sir,seed_graph

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

def simulate_sir(population_parameters,disease_parameters,model_parameters):
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
    recovered_population = []
    white_inf_pop = []
    white_rec_pop = []
    black_inf_pop = []
    black_rec_pop = []
    asian_inf_pop = []
    asian_rec_pop = []
    other_inf_pop = []
    other_rec_pop = []
    male_inf_pop = []
    male_rec_pop = []
    female_inf_pop = []
    female_rec_pop = []
    child_inf_pop = []
    child_rec_pop = []
    adult_inf_pop = []
    adult_rec_pop = []
    senior_inf_pop = []
    senior_rec_pop = []
    total_sus = []
    white_sus = []
    black_sus = []
    asian_sus = []
    other_sus = []
    male_sus = []
    female_sus = []
    child_sus = []
    adult_sus = []
    senior_sus = []
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
        recover_sir(active_nodes,G,recovery_parameters)
        data = count_all_sir(G)
        recovered_population.append(data['total_rec'])
        infected_population.append(data['total_inf'])
        white_rec_pop.append(data['white_rec'])
        white_inf_pop.append(data['white_inf'])
        black_rec_pop.append(data['black_rec'])
        black_inf_pop.append(data['black_inf'])
        asian_rec_pop.append(data['asian_rec'])
        asian_inf_pop.append(data['asian_inf'])
        other_rec_pop.append(data['other_rec'])
        other_inf_pop.append(data['other_inf'])
        male_rec_pop.append(data['male_rec'])
        male_inf_pop.append(data['male_inf'])
        female_rec_pop.append(data['female_rec'])
        female_inf_pop.append(data['female_inf'])
        child_rec_pop.append(data['child_rec'])
        child_inf_pop.append(data['child_inf'])
        adult_rec_pop.append(data['adult_rec'])
        adult_inf_pop.append(data['adult_inf'])
        senior_rec_pop.append(data['senior_rec'])
        senior_inf_pop.append(data['senior_inf'])
        total_sus.append(data['total_sus'])
        white_sus.append(data['white_sus'])
        black_sus.append(data['black_sus'])
        asian_sus.append(data['asian_sus'])
        other_sus.append(data['other_sus'])
        male_sus.append(data['male_sus'])
        female_sus.append(data['female_sus'])
        child_sus.append(data['child_sus'])
        adult_sus.append(data['adult_sus'])
        senior_sus.append(data['senior_sus'])
    data = {
        'rec_total':recovered_population,
        'inf_total':infected_population,
        'white_rec':white_rec_pop,
        'white_inf':white_inf_pop,
        'black_rec':black_rec_pop,
        'black_inf':black_inf_pop,
        'asian_rec':asian_rec_pop,
        'asian_inf':asian_inf_pop,
        'other_rec':other_rec_pop,
        'other_inf':other_inf_pop,
        'male_inf':male_inf_pop,
        'male_rec':male_rec_pop,
        'female_inf':female_inf_pop,
        'female_rec':female_rec_pop,
        'child_inf':child_inf_pop,
        'child_rec':child_rec_pop,
        'adult_inf':adult_inf_pop,
        'adult_rec':adult_rec_pop,
        'senior_inf':senior_inf_pop,
        'senior_rec':senior_rec_pop,
        'white_sus':white_sus,
        'black_sus':black_sus,
        'asian_sus':asian_sus,
        'other_sus':other_sus,
        'male_sus':male_sus,
        'female_sus':female_sus,
        'child_sus':child_sus,
        'adult_sus':adult_sus,
        'senior_sus':senior_sus,
        'sus_total':total_sus
    }       
    return data
