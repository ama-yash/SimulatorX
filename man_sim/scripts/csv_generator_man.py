import random

import networkx as nx
import numpy as np
import pandas as pd


def generateNodes(N, G, eth, gen, ag, flag):
    temp = N
    white_pop = round((N * eth["white"]) / 100)
    black_pop = round((N * eth["black"]) / 100)
    mixed_pop = round((N * eth["other"]) / 100)
    asian_pop = round((N * eth["asian"]) / 100)
    N = white_pop + black_pop + mixed_pop + asian_pop
    male_pop = round((N * gen["male"]) / 100)
    female_pop = round((N * gen["female"]) / 100)
    N = male_pop + female_pop
    child_pop = round((N * ag["child"]) / 100)
    adult_pop = round((N * ag["adult"]) / 100)
    senior_pop = round((N * ag["senior"]) / 100)
    N = child_pop + adult_pop + senior_pop
    if N != temp:
        N = temp
    if flag == 0:
        G.add_nodes_from(np.arange(0, N))
    nx.set_node_attributes(G, "S", "status")
    nodes_list = list(G.nodes)
    white_nodes = random.sample(nodes_list, int(white_pop))
    nodes_list = list(set(nodes_list) ^ set(white_nodes))
    black_nodes = random.sample(nodes_list, int(black_pop))
    nodes_list = list(set(nodes_list) ^ set(black_nodes))
    mixed_nodes = random.sample(nodes_list, int(mixed_pop))
    nodes_list = list(set(nodes_list) ^ set(mixed_nodes))
    asian_nodes = random.sample(nodes_list, int(asian_pop))
    for i in white_nodes:
        G.nodes[i]["ethnicity"] = 0
    for i in black_nodes:
        G.nodes[i]["ethnicity"] = 1
    for i in asian_nodes:
        G.nodes[i]["ethnicity"] = 2
    for i in mixed_nodes:
        G.nodes[i]["ethnicity"] = 3
    nodes_list = list(G.nodes)
    male_nodes = random.sample(nodes_list, int(male_pop))
    nodes_list = list(set(nodes_list) ^ set(male_nodes))
    female_nodes = random.sample(nodes_list, int(female_pop))
    for i in male_nodes:
        G.nodes[i]["gender"] = 0
    for i in female_nodes:
        G.nodes[i]["gender"] = 1
    nodes_list = list(G.nodes)
    child_nodes = random.sample(nodes_list, int(child_pop))
    nodes_list = list(set(nodes_list) ^ set(child_nodes))
    adult_nodes = random.sample(nodes_list, int(adult_pop))
    nodes_list = list(set(nodes_list) ^ set(adult_nodes))
    senior_nodes = random.sample(nodes_list, int(senior_pop))
    for i in child_nodes:
        G.nodes[i]["age"] = random.randint(1, 14)
    for i in adult_nodes:
        G.nodes[i]["age"] = random.randint(15, 54)
    for i in senior_nodes:
        G.nodes[i]["age"] = random.randint(55, 110)


def get_beta(node, G, infection_parameters):
    age = G.nodes[node]["age"]
    gender = G.nodes[node]["gender"]
    eth = G.nodes[node]["ethnicity"]
    if age >= 0 and age <= 14:
        age_p = infection_parameters["child_inf"]
    elif age >= 15 and age <= 54:
        age_p = infection_parameters["adult_inf"]
    elif age >= 55:
        age_p = infection_parameters["senior_inf"]
    male_p = infection_parameters["male_inf"]
    female_p = infection_parameters["female_inf"]
    white_p = infection_parameters["white_inf"]
    sa_p = infection_parameters["asian_inf"]
    black_p = infection_parameters["black_inf"]
    mixed_p = infection_parameters["other_inf"]
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


def generate_DataFrame():
    dff_test = pd.DataFrame(columns=["Ethnicity", "Gender", "Age", "Beta_Class"])
    return dff_test


def run(G, N, infection_parameters):
    dff_test = generate_DataFrame()
    eth = []
    gen = []
    age = []
    beta = []
    for n in range(0, N):
        beta_n = get_beta(n, G, infection_parameters)
        b = beta_n
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
        elif b > 0.2 and b < 0.21:
            b = 20
        elif b > 0.21 and b <= 0.22:
            b = 21
        elif b > 0.22 and b <= 0.23:
            b = 22
        elif b > 0.23 and b <= 0.24:
            b = 23
        elif b > 0.24 and b <= 0.25:
            b = 24
        elif b > 0.25 and b <= 0.26:
            b = 25
        elif b > 0.26 and b <= 0.27:
            b = 26
        elif b > 0.27 and b <= 0.28:
            b = 27
        elif b > 0.28 and b < 0.29:
            b = 28
        elif b > 0.29 and b < 0.3:
            b = 29
        elif b > 0.3 and b < 0.31:
            b = 30
        eth.append(G.nodes[n]["ethnicity"])
        gen.append(G.nodes[n]["gender"])
        age.append(G.nodes[n]["age"])
        beta.append(round(beta_n, 2))
    dff_test["Ethnicity"] = eth
    dff_test["Gender"] = gen
    dff_test["Age"] = age
    dff_test["Beta_Class"] = beta
    return dff_test


def generate_CSV(pop_parameters, infection_parameters, filepath):
    N = pop_parameters["N"]
    if infection_parameters["flag"] == 0:
        G = nx.Graph()
    else:
        G = nx.barabasi_albert_graph(N, infection_parameters["m"])
    ethn = {
        "white": pop_parameters["white"],
        "black": pop_parameters["black"],
        "asian": pop_parameters["asian"],
        "other": pop_parameters["other"],
    }
    gen = {"male": pop_parameters["male"], "female": pop_parameters["female"]}
    ag = {
        "child": pop_parameters["child"],
        "adult": pop_parameters["adult"],
        "senior": pop_parameters["senior"],
    }
    generateNodes(N, G, ethn, gen, ag, infection_parameters["flag"])
    dframe = run(G, N, infection_parameters)
    dframe = dframe[["Ethnicity", "Gender", "Age", "Beta_Class"]]
    dframe.to_csv(filepath, index=False)
