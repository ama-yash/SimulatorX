import random

import networkx as nx
import numpy as np
import pandas as pd

from count import count_all_sir
from cov19_simulation_tools import infect, loadDep, sir_recover
from gen_simulation_tools import init_sir_counts, seed_graph, update_sir_counts
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


def simulate_sir(parameters):
    N = parameters["N"]
    ethn = {
        "white": parameters["white"],
        "black": parameters["black"],
        "asian": parameters["asian"],
        "other": parameters["other"],
    }
    gen = {"male": parameters["male"], "female": parameters["female"]}
    ag = {
        "child": parameters["child"],
        "adult": parameters["adult"],
        "senior": parameters["senior"],
    }
    graph = {"code": 0}
    G = generateNodes(N, ethn, gen, ag, graph)
    dataframe = loadDep()
    epsilon = 0.001
    eta = 1.0
    gamma = -2.1
    act = power_law(epsilon, 1, gamma, N)
    count_dicts = init_sir_counts()
    m = 2
    seeds = float(parameters["seeds"])
    seed_graph(G, seeds)
    for i in range(parameters["time"]):
        active_nodes = activate_graph(act, G, N)
        for i in active_nodes:
            count = 0
            while count < m:
                target = random.randint(0, N - 1)
                if target != i and target not in G.neighbors(i):
                    G.add_edge(i, target)
                    count += 1
        infect(active_nodes, G, dataframe)
        sir_recover(active_nodes, G)
        data = count_all_sir(G)
        count_dicts = update_sir_counts(count_dicts, data)
    return count_dicts
