import random

from count import count_all_si
from covid_19_selectors import infect
from gen_simulation_tools import init_si_counts, update_si_counts
from genNode import generateNodes
from selector.selector import load_susceptibility_matrix, seed_graph, activate_graph, power_law


def simulate_si(parameters):
    N = int(parameters["pop_size"])

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
    graph = {
        "code": 0,
    }
    G = generateNodes(N, ethn, gen, ag, graph)
    dataframe = load_susceptibility_matrix()
    epsilon = 0.001

    gamma = -2.1
    act = power_law(epsilon, 1, gamma, N)
    count_dicts = init_si_counts()
    m = 2
    seeds = float(parameters["seeds"])
    seed_graph(G, seeds)
    time = int(parameters["time"])
    for t in range(time):
        active_nodes = activate_graph(act, N)
        for i in active_nodes:
            count = 0
            while count < m:
                target = random.randint(0, N - 1)
                if target != i and target not in G.neighbors(i):
                    G.add_edge(i, target)
                    count += 1
        infect(active_nodes, G, dataframe)
        data = count_all_si(G)
        count_dicts = update_si_counts(count_dicts, data)
    return count_dicts
