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
def init_si_counts():
    counts_list = ['inf_total', 'sus_total', 'white_sus', 'white_inf', 'black_sus', 'black_inf', 'asian_sus', 'asian_inf', 'other_sus', 'other_inf', 'male_inf', 'male_sus', 'female_inf', 'female_sus', 'child_inf', 'child_sus', 'adult_inf', 'adult_sus', 'senior_inf', 'senior_sus']
    count_dicts = {k:[] for k in counts_list}
    return count_dicts

def init_sir_counts():
    counts_list = ['inf_total', 'sus_total', 'rec_total', 'white_sus', 'white_rec', 'white_inf', 'black_sus','black_rec', 'black_inf', 'asian_sus','asian_rec', 'asian_inf', 'other_sus', 'other_rec', 'other_inf', 'male_inf','male_rec', 'male_sus', 'female_inf', 'female_rec', 'female_sus', 'child_inf','child_rec', 'child_sus', 'adult_inf','adult_rec', 'adult_sus', 'senior_inf', 'senior_rec', 'senior_sus']
    count_dicts = {k:[] for k in counts_list}
    return count_dicts

def update_sir_counts(count_dicts,data):
    count_dicts['sus_total'].append(data['total_sus'])
    count_dicts['inf_total'].append(data['total_inf'])
    count_dicts['rec_total'].append(data['total_rec']) 
    count_dicts['white_sus'].append(data['white_sus'])
    count_dicts['white_inf'].append(data['white_inf'])
    count_dicts['white_rec'].append(data['white_rec']) 
    count_dicts['black_sus'].append(data['black_sus'])
    count_dicts['black_inf'].append(data['black_inf'])
    count_dicts['black_rec'].append(data['black_rec'])
    count_dicts['asian_sus'].append(data['asian_sus'])
    count_dicts['asian_inf'].append(data['asian_inf'])
    count_dicts['asian_rec'].append(data['asian_rec'])
    count_dicts['other_sus'].append(data['other_sus'])
    count_dicts['other_inf'].append(data['other_inf'])
    count_dicts['other_rec'].append(data['other_rec'])
    count_dicts['male_sus'].append(data['male_sus'])
    count_dicts['male_inf'].append(data['male_inf'])
    count_dicts['male_rec'].append(data['male_rec'])
    count_dicts['female_sus'].append(data['female_sus'])
    count_dicts['female_inf'].append(data['female_inf'])
    count_dicts['female_rec'].append(data['female_rec'])
    count_dicts['child_sus'].append(data['child_sus'])
    count_dicts['child_inf'].append(data['child_inf'])
    count_dicts['child_rec'].append(data['child_rec'])
    count_dicts['adult_sus'].append(data['adult_sus'])
    count_dicts['adult_inf'].append(data['adult_inf'])
    count_dicts['adult_rec'].append(data['adult_rec'])
    count_dicts['senior_sus'].append(data['senior_sus'])
    count_dicts['senior_inf'].append(data['senior_inf'])
    count_dicts['senior_rec'].append(data['senior_rec'])
    return count_dicts
def update_si_counts(count_dicts,data):
    count_dicts['sus_total'].append(data['total_sus'])
    count_dicts['inf_total'].append(data['total_inf'])
    count_dicts['white_sus'].append(data['white_sus'])
    count_dicts['white_inf'].append(data['white_inf'])
    count_dicts['black_sus'].append(data['black_sus'])
    count_dicts['black_inf'].append(data['black_inf'])
    count_dicts['asian_sus'].append(data['asian_sus'])
    count_dicts['asian_inf'].append(data['asian_inf'])
    count_dicts['other_sus'].append(data['other_sus'])
    count_dicts['other_inf'].append(data['other_inf'])
    count_dicts['male_sus'].append(data['male_sus'])
    count_dicts['male_inf'].append(data['male_inf'])
    count_dicts['female_sus'].append(data['female_sus'])
    count_dicts['female_inf'].append(data['female_inf'])
    count_dicts['child_sus'].append(data['child_sus'])
    count_dicts['child_inf'].append(data['child_inf'])
    count_dicts['adult_sus'].append(data['adult_sus'])
    count_dicts['adult_inf'].append(data['adult_inf'])
    count_dicts['senior_sus'].append(data['senior_sus'])
    count_dicts['senior_inf'].append(data['senior_inf'])
    return count_dicts
