import random

import pandas as pd


def read_file(filename):
    data = {}
    with open(filename, "r+") as text:
        for line in text.readlines():
            key, value = line.strip().split(",")
            data[key] = value

    return data


def round_number(N, percentage):
    return round((float(percentage) / 100.0) * float(N))


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


def seed_graph(G, seeds):
    nodes = G.number_of_nodes()
    number_of_seeds = int(nodes * (int(seeds) / 100))
    rand_nodes = random.sample(range(nodes), int(number_of_seeds))
    for n in range(0, nodes):
        if n in rand_nodes:
            G.nodes[n]["status"] = "I"
        else:
            G.nodes[n]["status"] = "S"


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


def activate_graph(activity, N):
    active_nodes = []
    for i in range(N):
        if random.random() < activity[i]:
            active_nodes.append(i)
    return active_nodes


def load_susceptibility_matrix():
    return pd.read_csv("datasets/susceptibility_matrix2.csv")


def load_recovery_matrix():
    return pd.read_csv("datasets/recovery_matrix.csv", index_col=0)


def get_susceptibility_matrix_index(age):
    """
    The age matrix is 16x16 and it's split in groups of 4,
    We can use whole division to quickly get the index
    """
    if age >= 75:
        return 15
    else:
        return age // 5


def get_recovery_rate_from_matrix(gender, age):
    nodes_recovery = load_recovery_matrix()

    if gender == 0:
        column = "Male"
    elif gender == 1:
        column = "Female"

    if age <= 19:
        return nodes_recovery.loc[column][0]
    elif age >= 60:
        return nodes_recovery.loc[column][5]
    else:
        return nodes_recovery.loc[column][(age // 10) - 1]


def get_infection_rate(nodeA, nodeB, G):
    dataframe = load_susceptibility_matrix()

    ageA = G.nodes[nodeA]["age"]
    ageB = G.nodes[nodeB]["age"]
    gender = G.nodes[nodeA]["gender"]
    ethnicity = G.nodes[nodeA]["ethnicity"]

    row = get_susceptibility_matrix_index(ageA)
    col = get_susceptibility_matrix_index(ageB)

    age_infection_rate = dataframe.iloc[row, col]

    # infection probabilities for populations
    gender_infection_rate = [0.17, 0.146]  # male, female infection rates
    population_infection_rate = [
        0.7392,
        0.8618,
        0.4927,
        0.8799,
    ]  # white, black, mixed, asian

    return (
        age_infection_rate
        * gender_infection_rate[gender]
        * population_infection_rate[ethnicity]
    )


def get_recovery_rate(node, G):
    age = G.nodes[node]["age"]
    gender = G.nodes[node]["gender"]
    ethnicity = G.nodes[node]["ethnicity"]

    population_recover_rate = [
        0.1585,
        0.2910,
        0.1923,
        0.1585,
    ]  # white, black, mixed, asian

    gender_recover_rate = get_recovery_rate_from_matrix(gender, age)

    return gender_recover_rate * population_recover_rate[ethnicity]


def infect(active_nodes, G, infection_rate=None):
    for n in active_nodes:
        neighbors = list(G.neighbors(n))
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if G.nodes[n]["status"] == "S":
                    if not infection_rate:
                        # use covid infection rates if None is set
                        infection_rate = get_infection_rate(n, neighbor, G) - 0.076
                    if random.uniform(0, 1) < infection_rate:
                        G.nodes[n]["status"] = "I"


def recover(active_nodes, G, recovery_rate=None, permanent_recovery=False):
    for n in active_nodes:
        if G.nodes[n]["status"] == "I":
            if not recovery_rate:
                # use covid recovery rates is None is set
                recovery_rate = get_recovery_rate(n, G)
            if random.uniform(0, 1) < recovery_rate:
                if permanent_recovery:
                    G.nodes[n]["status"] = "R"
                else:
                    G.nodes[n]["status"] = "S"
