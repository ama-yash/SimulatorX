import random

import pandas as pd
from covid_19_selectors import get_beta
from genNode import generateNodes
from selector.selector import load_susceptibility_matrix


def generate_DataFrame():
    return pd.DataFrame(
        columns=["Ethnicity", "Gender", "Target_Age", "Source_Age", "Beta_Class"]
    )


def run(G, N, dataframe):
    df = generate_DataFrame()
    ethnicity_list = []
    gender_list = []
    node_i_age_list = []
    node_j_age_list = []
    beta_list = []
    for n in range(0, N):
        random_target = int(random.randint(0, N - 1))
        node_j_age = G.nodes[random_target]["age"]
        beta = get_beta(n, node_j_age, G, dataframe)
        if beta < 0.2:
            beta = beta * 100

        ethnicity_list.append(G.nodes[n]["ethnicity"])
        gender_list.append(G.nodes[n]["gender"])
        node_i_age_list.append(G.nodes[n]["age"])
        node_j_age_list.append(node_j_age)
        beta_list.append(beta)

    df["Ethnicity"] = ethnicity_list
    df["Gender"] = gender_list
    df["Target_Age"] = node_i_age_list
    df["Source_Age"] = node_j_age_list
    df["Beta_Class"] = beta_list

    return df


def generate_CSV(parameters, filepath):
    N = int(parameters["pop_size"])
    susceptibility_matrix = load_susceptibility_matrix()
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
    graph = {"code": 1, "m": 2}
    G = generateNodes(N, ethn, gen, ag, graph)

    dframe = run(G, N, susceptibility_matrix)

    dframe = dframe[["Ethnicity", "Gender", "Target_Age", "Source_Age", "Beta_Class"]]

    dframe.to_csv(filepath, index=False)
