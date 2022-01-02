import random
import networkx as nx

def get_beta(node,G,infection_parameters):
    age = G.nodes[node]['age']
    gender = G.nodes[node]['gender']
    eth = G.nodes[node]['ethnicity']
    if age >=0 and age <= 14:
        age_p = infection_parameters['child']
    elif age >= 15 and age <=54:
        age_p = infection_parameters['adult']
    elif age >= 55:
        age_p = infection_parameters['senior']
    male_p = infection_parameters['male']
    female_p = infection_parameters['female']
    white_p = infection_parameters['white']
    sa_p = infection_parameters['asian']
    black_p = infection_parameters['black']
    mixed_p = infection_parameters['other']
    if eth == 0:
        if gender == 0:
            beta = age_p * male_p * sa_p
        else:
            beta = age_p * female_p * sa_p
    elif eth == 1:
        if gender == 0:
            beta = age_p * male_p * black_p
        else:
            beta = age_p * female_p * black_p
    elif eth == 2:
        if gender == 0:
            beta = age_p * male_p * white_p
        else:
            beta = age_p * female_p * white_p
    elif eth == 3:
        if gender == 0:
            beta = age_p * male_p * mixed_p
        else:
            beta = age_p * female_p * mixed_p
    return beta
def get_rec(node,G,recovery_parameters):
    age = G.nodes[node]['age']
    gender = G.nodes[node]['gender']
    eth = G.nodes[node]['ethnicity']
    white_p = recovery_parameters['white']
    sa_p = recovery_parameters['asian']
    black_p = recovery_parameters['black']
    mixed_p = recovery_parameters['other']
    male_p = recovery_parameters['male']
    female_p = recovery_parameters['female']
    if age >=0 and age <= 14:
        age_p = recovery_parameters['child']
    elif age >= 15 and age <=54:
        age_p = recovery_parameters['adult']
    elif age >= 55:
        age_p = recovery_parameters['senior']
    if eth == 0:
        if gender == 0:
            gamma = age_p * male_p * sa_p
        else:
            gamma = age_p * female_p * sa_p
    elif eth == 1:
        if gender == 0:
            gamma = age_p * male_p * black_p
        else:
            gamma = age_p * female_p * black_p
    elif eth == 2:
        if gender == 0:
            gamma = age_p * male_p * white_p
        else:
            gamma = age_p * female_p * white_p
    elif eth == 3:
        if gender == 0:
            gamma = age_p * male_p * mixed_p
        else:
            gamma = age_p * female_p * mixed_p
    return gamma

def seed_graph(G, seeds):
    nodes = G.number_of_nodes()
    seeds_int = int((nodes*seeds)/100)
    rand_nodes = random.sample(range(nodes), seeds_int)
    for n in range(0, nodes):
        if n in rand_nodes:
            G.nodes[n]['status'] = 'I'
        else:
            G.nodes[n]['status'] = 'S'

def infect(a_nodes,G,infection_parameters):
    for n in a_nodes:
        neighbors = list(G.neighbors(n))
        for neighbor in neighbors:
            if G.nodes[n]['status'] == 'S':
                con = G.nodes[neighbor]['age']
                if random.uniform(0,1) < get_beta(n,G,infection_parameters):
                    G.nodes[n]['status'] = 'I'
def recover_sir(a_nodes,G,recovery_parameters):
    for n in a_nodes:
        if G.nodes[n]['status'] == 'I':
            if random.uniform(0,1) < get_rec(n,G,recovery_parameters):
                G.nodes[n]['status'] = 'R'
def recover_sis(a_nodes,G,recovery_parameters):
    for n in a_nodes:
        if G.nodes[n]['status'] == 'I':
            if random.uniform(0,1) < get_rec(n,G,recovery_parameters):
                G.nodes[n]['status'] = 'S'
