import numpy as np
import random
import networkx as nx

def generateNodes(N,eth,gen,ag,graph):
    temp = N
    white_pop = round((N * eth['white']) / 100)
    black_pop = round((N * eth['black']) / 100)
    mixed_pop = round((N * eth['other']) / 100)
    asian_pop = round((N * eth['asian']) / 100)
    N = white_pop + black_pop + mixed_pop + asian_pop
    if N < temp:
        diff = temp - N
        asian_pop += diff
        N = white_pop + black_pop + mixed_pop + asian_pop
    elif N > temp:
        diff = N - temp
        asian_pop -= diff
        N = white_pop + black_pop + mixed_pop + asian_pop
    temp = N
    male_pop = round((N * gen['male']) / 100)
    female_pop = round((N * gen['female']) / 100)
    N = male_pop + female_pop
    if N < temp:
        diff = temp - N
        female_pop += diff
        N = male_pop + female_pop
    elif N > temp:
        diff = N - temp
        female_pop -= diff
        N = male_pop + female_pop
    temp = N
    child_pop = round((N * ag['child']) / 100)
    adult_pop = round((N * ag['adult']) / 100)
    senior_pop = round((N * ag['senior']) / 100)
    N = child_pop + adult_pop + senior_pop      
    if N < temp:
        diff = temp - N
        senior_pop += diff
        N = child_pop + adult_pop + senior_pop
    elif N > temp:
        diff = N - temp
        senior_pop -= diff
        N = child_pop + adult_pop + senior_pop
    if graph['code'] == 0:
        G = nx.Graph()
        G.add_nodes_from(np.arange(0,N))
    elif graph['code'] == 1:
        G = nx.barabasi_albert_graph(N,graph['m'])
    nx.set_node_attributes(G,'S','status')
    nodes_list = list(G.nodes)
    white_nodes = random.sample(nodes_list,white_pop)
    nodes_list = list(set(nodes_list)^set(white_nodes))
    black_nodes = random.sample(nodes_list,black_pop)
    nodes_list = list(set(nodes_list)^set(black_nodes))
    mixed_nodes = random.sample(nodes_list,mixed_pop)
    nodes_list = list(set(nodes_list)^set(mixed_nodes))
    asian_nodes = random.sample(nodes_list,asian_pop)
    for i in white_nodes:
        G.nodes[i]['ethnicity'] = 0
    for i in black_nodes:
        G.nodes[i]['ethnicity'] = 1
    for i in asian_nodes:
        G.nodes[i]['ethnicity'] = 2
    for i in mixed_nodes:
        G.nodes[i]['ethnicity'] = 3
    nodes_list = list(G.nodes)
    male_nodes = random.sample(nodes_list,male_pop)
    nodes_list = list(set(nodes_list)^set(male_nodes))
    female_nodes = random.sample(nodes_list,female_pop)
    for i in male_nodes:
        G.nodes[i]['gender'] = 0
    for i in female_nodes:
        G.nodes[i]['gender'] = 1
    nodes_list = list(G.nodes)
    child_nodes = random.sample(nodes_list,child_pop)
    nodes_list = list(set(nodes_list)^set(child_nodes))
    adult_nodes = random.sample(nodes_list,adult_pop)
    nodes_list = list(set(nodes_list)^set(adult_nodes))
    senior_nodes = random.sample(nodes_list,senior_pop)
    for i in child_nodes:
        G.nodes[i]['age'] = random.randint(1,14)
    for i in adult_nodes:
        G.nodes[i]['age'] = random.randint(15,54)
    for i in senior_nodes:
        G.nodes[i]['age'] = random.randint(55,110)
    return G
