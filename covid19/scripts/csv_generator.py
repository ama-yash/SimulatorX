import random

import networkx as nx
import pandas as pd
from demographic_graph_generator import generate_nodes
from selector.selector import load_susceptibility_matrix, get_infection_rate


def generate_dataFrame():
    return pd.DataFrame(
        columns=["Ethnicity", "Gender", "Target_Age", "Source_Age", "Beta_Class"]
    )


def run(G, N):
    df = generate_dataFrame()
    ethnicity_list = []
    gender_list = []
    node_i_age_list = []
    node_j_age_list = []
    beta_list = []
    for n in range(0, N):
        random_target = int(random.randint(0, N - 1))
        target_node = G.nodes[random_target]["age"]
        beta = get_infection_rate(n, target_node, G)
        if beta < 0.2:
            beta = beta * 100

        ethnicity_list.append(G.nodes[n]["ethnicity"])
        gender_list.append(G.nodes[n]["gender"])
        node_i_age_list.append(G.nodes[n]["age"])
        node_j_age_list.append(target_node)
        beta_list.append(beta)

    df["Ethnicity"] = ethnicity_list
    df["Gender"] = gender_list
    df["Target_Age"] = node_i_age_list
    df["Source_Age"] = node_j_age_list
    df["Beta_Class"] = beta_list

    return df


def generate_csv(parameters, filepath):
    N = int(parameters["pop_size"])

    ethnicity = {
        "white": parameters["white"],
        "black": parameters["black"],
        "asian": parameters["asian"],
        "other": parameters["other"],
    }
    gender = {"male": parameters["male"], "female": parameters["female"]}
    age = {
        "child": parameters["child"],
        "adult": parameters["adult"],
        "senior": parameters["senior"],
    }
    G = nx.empty_graph(N)

    G = generate_nodes(G, ethnicity, gender, age)

    df = run(G, N)

    df = df[["Ethnicity", "Gender", "Target_Age", "Source_Age", "Beta_Class"]]

    df.to_csv(filepath, index=False)

    return age, gender, ethnicity
