import random
from selector.selector import infection_rate, recovery_rate

def get_beta(nodeA, nodeB, G, dataframe):
    return infection_rate(nodeA, nodeB, G, dataframe)

def get_rec(node, G):
    return recovery_rate(node, G)

def infect(a_nodes,G,dataframe):
    for n in a_nodes:
        neighbors = list(G.neighbors(n))
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if G.nodes[n]['status'] == 'S':
                    if random.uniform(0,1) < (get_beta(n,neighbor,G,dataframe) - 0.08):
                        G.nodes[n]['status'] = 'I'
def sis_recover(a_nodes,G):
    for n in a_nodes:
        if G.nodes[n]['status'] == 'I':
            if random.uniform(0,1) < get_rec(n,G):
                G.nodes[n]['status'] = 'S'
def si_recover(a_nodes,G):
    for n in a_nodes:
        if G.nodes[n]['status'] == 'I':
            if random.uniform(0,1) < get_rec(n,G):
                G.nodes[n]['status'] = 'S'
def sir_recover(a_nodes,G):
    for n in a_nodes:
        if G.nodes[n]['status'] == 'I':
            if random.uniform(0,1) < get_rec(n,G):
                G.nodes[n]['status'] = 'R'