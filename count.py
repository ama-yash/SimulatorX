from collections import Counter
import networkx as nx
import pandas as pd

def count_compartament_data(G):
    graph_attributes = nx.get_node_attributes(G, "status")
    status_counts = Counter(graph_attributes.values())
    return status_counts  # return the number of susceptible and infected

def count_attributes(G):

    dod = {}  # dict of dicts
    for node in G.nodes:
        dod[node] = G.nodes[node]

    df = pd.DataFrame(dod).transpose()  # swap rows and columns

    '''
        Ethnicity
        # 0 - white_population
        # 1 - black_population
        # 2 - mixed_population
        # 3 - asian_population
    '''

    '''
        Gender
        # 0 - male_population
        # 1 - female_population
    '''

    '''
        Age 
        youth 1 < age < 14,
        adult 15 < age < 54,
        senior 55 < age < 110
    '''

    data = {
        "total_inf": len(df.query("status == 'I'")),
        "total_sus": len(df.query("status == 'S'")),
        "total_rec": len(df.query("status == 'R'")),

        "white_inf": len(df.query("status == 'I' and ethnicity == 0")),
        "white_sus": len(df.query("status == 'S' and ethnicity == 0")),
        "white_rec": len(df.query("status == 'R' and ethnicity == 0")),

        "black_inf": len(df.query("status == 'I' and ethnicity == 1")),
        "black_sus": len(df.query("status == 'S' and ethnicity == 1")),
        "black_rec": len(df.query("status == 'R' and ethnicity == 1")),

        "other_inf": len(df.query("status == 'I' and ethnicity == 2")),
        "other_sus": len(df.query("status == 'S' and ethnicity == 2")),
        "other_rec": len(df.query("status == 'R' and ethnicity == 2")),

        "asian_inf": len(df.query("status == 'I' and ethnicity == 3")),
        "asian_sus": len(df.query("status == 'S' and ethnicity == 3")),
        "asian_rec": len(df.query("status == 'R' and ethnicity == 3")),

        "male_sus": len(df.query("status == 'S' and gender == 0")),
        "male_inf": len(df.query("status == 'I' and gender == 0")),
        "male_rec": len(df.query("status == 'R' and gender == 0")),

        "female_sus": len(df.query("status == 'S' and gender == 1")),
        "female_inf": len(df.query("status == 'I' and gender == 1")),
        "female_rec": len(df.query("status == 'R' and gender == 1")),

        "child_inf": len(df.query("status == 'I' and 1 < age < 14")),
        "child_sus": len(df.query("status == 'S' and 1 < age < 14")),
        "child_rec": len(df.query("status == 'R' and 1 < age < 14")),

        "adult_inf": len(df.query("status == 'I' and 15 < age < 54")),
        "adult_sus": len(df.query("status == 'S' and 15 < age < 54")),
        "adult_rec": len(df.query("status == 'R' and 15 < age < 54")),

        "senior_inf": len(df.query("status == 'I' and 55 < age < 110")),
        "senior_sus": len(df.query("status == 'S' and 55 < age < 110")),
        "senior_rec": len(df.query("status == 'R' and 55 < age < 110")),
    }

    return data

def count_data(model_data, data):
    for key, value in data.items():
        model_data[key].append(value)

    return model_data