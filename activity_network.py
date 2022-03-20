from selector.selector import activate_graph, power_law
import random


def generate_activity_network(G, N, neighbours_to_infect):
    epsilon = 0.001
    gamma = -2.1

    act = power_law(epsilon, 1, gamma, N)  # create node activity distribution

    active_nodes = activate_graph(act, N)

    for i in active_nodes:
        count = 0
        while count < neighbours_to_infect:
            target = random.randint(0, N - 1)
            if target != i and target not in G.neighbors(i):
                G.add_edge(i, target)
                count += 1
    return G, active_nodes
