import random

import networkx as nx
import numpy as np
import pandas as pd

from count import count_all_si
from gen_simulation_tools import (
    infect,
    init_si_counts,
    recover_sis,
    seed_graph,
    update_si_counts,
)
from genNode import generateNodes


def power_law(x0, x1, gamma, N):
    pl = []
    for i in range(N):
        pl.append(
            (
                (x1 ** (gamma + 1) - x0 ** (gamma + 1)) * random.uniform(0, 1)
                + x0 ** (gamma + 1.0)
            )
            ** (1.0 / (gamma + 1.0))
        )
    return pl


def activate_graph(activity, graph, N):
    active_nodes = []
    for i in range(N):
        if random.random() < activity[i]:
            active_nodes.append(i)
    return active_nodes


def simulate_sis(population_parameters, disease_parameters, model_parameters):
    N = population_parameters["N"]
    ethn = {
        "white": population_parameters["white"],
        "black": population_parameters["black"],
        "asian": population_parameters["asian"],
        "other": population_parameters["other"],
    }
    gen = {
        "male": population_parameters["male"],
        "female": population_parameters["female"],
    }
    ag = {
        "child": population_parameters["child"],
        "adult": population_parameters["adult"],
        "senior": population_parameters["senior"],
    }
    infection_parameters = {
        "white": disease_parameters["white_inf"],
        "black": disease_parameters["black_inf"],
        "asian": disease_parameters["asian_inf"],
        "other": disease_parameters["other_inf"],
        "male": disease_parameters["male_inf"],
        "female": disease_parameters["female_inf"],
        "child": disease_parameters["child_inf"],
        "adult": disease_parameters["adult_inf"],
        "senior": disease_parameters["senior_inf"],
    }
    recovery_parameters = {
        "white": disease_parameters["white_rec"],
        "black": disease_parameters["black_rec"],
        "asian": disease_parameters["asian_rec"],
        "other": disease_parameters["other_rec"],
        "male": disease_parameters["male_rec"],
        "female": disease_parameters["female_rec"],
        "child": disease_parameters["child_rec"],
        "adult": disease_parameters["adult_rec"],
        "senior": disease_parameters["senior_rec"],
    }
    g_type = model_parameters["graph_type"]
    if g_type == 0:
        graph = {
            "code": g_type,
        }
        m = 2
    elif g_type == 1:
        graph = {"code": g_type, "m": model_parameters["m"]}
        m = model_parameters["m"]
    G = generateNodes(N, ethn, gen, ag, graph)
    epsilon = 0.001
    eta = 1.0
    gamma = -2.1
    act = power_law(epsilon, 1, gamma, N)
    count_dicts = init_si_counts()
    seeds = int(model_parameters["seeds"])
    seed_graph(G, seeds)
    for i in range(model_parameters["time"]):
        if g_type == 0:
            active_nodes = activate_graph(act, G, N)
            for i in active_nodes:
                count = 0
                while count < m:
                    target = random.randint(0, N - 1)
                    if target != i and target not in G.neighbors(i):
                        G.add_edge(i, target)
                        count += 1
        else:
            active_nodes = G.nodes()
        infect(active_nodes, G, infection_parameters)
        recover_sis(active_nodes, G, recovery_parameters)
        data = count_all_si(G)
        count_dicts = update_si_counts(count_dicts, data)
    return count_dicts
