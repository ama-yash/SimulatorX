import random

import networkx as nx
import numpy as np
from selector.selector import round_number


def generateNodes(N, ethnicity, gender, age, graph_code,m):

    N = int(N)

    white_population = round_number(N, ethnicity.get("white"))
    black_population = round_number(N, ethnicity.get("black"))
    mixed_population = round_number(N, ethnicity.get("other"))
    asian_population = round_number(N, ethnicity.get("asian"))

    male_population = round_number(N, gender.get("male"))
    female_population = round_number(N, gender.get("female"))

    youth_population = round_number(N, age.get("child"))
    adult_population = round_number(N, age.get("adult"))
    senior_population = round_number(N, age.get("senior"))

    # generate graph

    if graph_code == 0:
        G = nx.Graph()
        G.add_nodes_from(np.arange(0, N))
    elif graph_code == 1:
        G = nx.barabasi_albert_graph(N, m)

    # set all nodes to susceptible
    nx.set_node_attributes(G, "S", "status")

    nodes_list = list(G.nodes)
    random.shuffle(nodes_list)  # randomize the list of nodes

    # partition the list of nodes into uneven list of lists
    partitions = [
        white_population,
        black_population,
        mixed_population,
        asian_population,
    ]
    nodes_parts = np.split(nodes_list, np.cumsum(partitions))

    # split the graph population into 4 ethnic groups
    wn_dict = {n: {"ethnicity": 0} for n in nodes_parts[0]}  # 0 - white_population
    bn_dict = {n: {"ethnicity": 1} for n in nodes_parts[1]}  # 1 - black_population
    mn_dict = {n: {"ethnicity": 2} for n in nodes_parts[2]}  # 2 - mixed_population
    an_dict = {n: {"ethnicity": 3} for n in nodes_parts[3]}  # 3 - asian_population

    gender_partitions = [male_population, female_population]
    gender_nodes_parts = np.split(nodes_list, np.cumsum(gender_partitions))

    male_dict = {n: {"gender": 0} for n in gender_nodes_parts[0]}  # 0 - male_population
    female_dict = {
        n: {"gender": 1} for n in gender_nodes_parts[1]
    }  # 1 - female_population

    age_partitions = [youth_population, adult_population, senior_population]
    age_nodes_parts = np.split(nodes_list, np.cumsum(age_partitions))

    """
        Generate age for the population such that age:
        youth 1 < age < 14,
        adult 15 < age < 54,
        senior 55 < age < 110
    """

    youth_dict = {n: {"age": random.randint(1, 14)} for n in age_nodes_parts[0]}
    adult_dict = {n: {"age": random.randint(15, 54)} for n in age_nodes_parts[1]}
    senior_dict = {n: {"age": random.randint(55, 110)} for n in age_nodes_parts[2]}

    # set generated attributes
    nx.set_node_attributes(G, wn_dict)
    nx.set_node_attributes(G, bn_dict)
    nx.set_node_attributes(G, mn_dict)
    nx.set_node_attributes(G, an_dict)

    nx.set_node_attributes(G, male_dict)
    nx.set_node_attributes(G, female_dict)

    nx.set_node_attributes(G, youth_dict)
    nx.set_node_attributes(G, adult_dict)
    nx.set_node_attributes(G, senior_dict)

    return G
