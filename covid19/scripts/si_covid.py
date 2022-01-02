import pandas as pd
import random
import numpy as np
import networkx as nx
from genNode import generateNodes
from count import count_all_si
from cov19_simulation_tools import infect,loadDep
from gen_simulation_tools import seed_graph

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

def simulate_si(parameters):
    N = parameters['N']
    ethn = {'white':parameters['white'],'black':parameters['black'],'asian':parameters['asian'],'other':parameters['other']}
    gen = {'male':parameters['male'],'female':parameters['female']}
    ag = {'child':parameters['child'],'adult':parameters['adult'],'senior':parameters['senior']}
    graph = {
        'code':0,
    }
    G = generateNodes(N,ethn,gen,ag,graph)
    dataframe = loadDep()
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
    m=2
    seeds = float(parameters['seeds'])
    seed_graph(G,seeds)
    for i in range(parameters['time']):
        active_nodes = activate_graph(act,G,N)
        for i in active_nodes:
          count=0
          while count<m:
              target=random.randint(0,N-1)
              if target!=i and target not in G.neighbors(i):
                  G.add_edge(i,target)
                  count+=1
        infect(active_nodes,G,dataframe)
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
