import pandas as pd
import random
import numpy as np
import networkx as nx
from genNode import generateNodes
from cov19_simulation_tools import infect,sis_recover,loadDep
from gen_simulation_tools import seed_graph, init_si_counts, update_si_counts
from count import count_all_si

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

def simulate_sis(parameters):
    N = parameters['N']
    print(N)
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
    count_dicts = init_si_counts()
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
        sis_recover(active_nodes,G)
        data = count_all_si(G)
        count_dicts = update_si_counts(count_dicts,data)
    return count_dicts
