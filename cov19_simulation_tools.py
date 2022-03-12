import random

import pandas as pd

from count import *


def loadDep():
    dataframe = pd.read_csv(
        "https://raw.githubusercontent.com/ama-yash/dataset/main/susceptibility_matrix2.csv"
    )
    return dataframe


def get_beta(nodeA, nodeB, G, dataframe):
    ageA = G.nodes[nodeA]["age"]
    ageB = G.nodes[nodeB]["age"]
    gender = G.nodes[nodeA]["gender"]
    eth = G.nodes[nodeA]["ethnicity"]
    if ageA >= 0 and ageA <= 5:
        row = 0
    elif ageA > 5 and ageA <= 10:
        row = 1
    elif ageA > 10 and ageA <= 15:
        row = 2
    elif ageA > 15 and ageA <= 20:
        row = 3
    elif ageA > 20 and ageA <= 25:
        row = 4
    elif ageA > 25 and ageA <= 30:
        row = 5
    elif ageA > 30 and ageA <= 35:
        row = 6
    elif ageA > 35 and ageA <= 40:
        row = 7
    elif ageA > 40 and ageA <= 45:
        row = 8
    elif ageA > 45 and ageA <= 50:
        row = 9
    elif ageA > 50 and ageA <= 55:
        row = 10
    elif ageA > 55 and ageA <= 60:
        row = 11
    elif ageA > 60 and ageA <= 65:
        row = 12
    elif ageA > 65 and ageA <= 70:
        row = 13
    elif ageA > 70 and ageA <= 75:
        row = 14
    elif ageA > 75:
        row = 15
    if ageB >= 0 and ageB <= 5:
        col = 0
    elif ageB > 5 and ageB <= 10:
        col = 1
    elif ageB > 10 and ageB <= 15:
        col = 2
    elif ageB > 15 and ageB <= 20:
        col = 3
    elif ageB > 20 and ageB <= 25:
        col = 4
    elif ageB > 25 and ageB <= 30:
        col = 5
    elif ageB > 30 and ageB <= 35:
        col = 6
    elif ageB > 35 and ageB <= 40:
        col = 7
    elif ageB > 40 and ageB <= 45:
        col = 8
    elif ageB > 45 and ageB <= 50:
        col = 9
    elif ageB > 50 and ageB <= 55:
        col = 10
    elif ageB > 55 and ageB <= 60:
        col = 11
    elif ageB > 60 and ageB <= 65:
        col = 12
    elif ageB > 65 and ageB <= 70:
        col = 13
    elif ageB > 70 and ageB <= 75:
        col = 14
    elif ageB > 75:
        col = 15
    age_p = dataframe.iloc[row, col]
    male_p = 0.17
    female_p = 0.146
    white_p = 0.7392  # 0
    sa_p = 0.8799  # 3
    black_p = 0.8618  # 1
    mixed_p = 0.4927  # 2
    if eth == 0:
        if gender == 0:
            beta = age_p * male_p * sa_p
        else:
            beta = age_p * female_p * sa_p
    elif eth == 1:
        if gender == 0:
            beta = age_p * male_p * black_p
        else:
            beta = age_p * female_p * black_p
    elif eth == 2:
        if gender == 0:
            beta = age_p * male_p * white_p
        else:
            beta = age_p * female_p * white_p
    elif eth == 3:
        if gender == 0:
            beta = age_p * male_p * mixed_p
        else:
            beta = age_p * female_p * mixed_p
    return beta


def get_rec(node, G):
    age = G.nodes[node]["age"]
    gender = G.nodes[node]["gender"]
    eth = G.nodes[node]["ethnicity"]
    white_p = 0.1585
    sa_p = 0.1428
    black_p = 0.2910
    mixed_p = 0.1923
    if gender == 0:
        if age >= 0 and age <= 19:
            rec = 0.073
        elif age > 19 and age <= 29:
            rec = 0.071
        elif age > 29 and age <= 39:
            rec = 0.069
        elif age > 39 and age <= 49:
            rec = 0.067
        elif age > 49 and age <= 59:
            rec = 0.068
        elif age >= 60:
            rec = 0.068
    if gender == 1:
        if age >= 0 and age <= 19:
            rec = 0.075
        elif age > 19 and age <= 29:
            rec = 0.071
        elif age > 29 and age <= 39:
            rec = 0.070
        elif age > 39 and age <= 49:
            rec = 0.067
        elif age > 49 and age <= 59:
            rec = 0.070
        elif age >= 60:
            rec = 0.071
    if eth == 0:
        rec = rec * sa_p
    elif eth == 1:
        rec = rec * black_p
    elif eth == 2:
        rec = rec * white_p
    elif eth == 3:
        rec = rec * mixed_p
    return rec


def infect(a_nodes, G, dataframe):
    for n in a_nodes:
        neighbors = list(G.neighbors(n))
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if G.nodes[n]["status"] == "S":
                    if random.uniform(0, 1) < (
                        get_beta(n, neighbor, G, dataframe) - 0.08
                    ):
                        G.nodes[n]["status"] = "I"


def sis_recover(a_nodes, G):
    for n in a_nodes:
        if G.nodes[n]["status"] == "I":
            if random.uniform(0, 1) < get_rec(n, G):
                G.nodes[n]["status"] = "S"


def si_recover(a_nodes, G):
    for n in a_nodes:
        if G.nodes[n]["status"] == "I":
            if random.uniform(0, 1) < get_rec(n, G):
                G.nodes[n]["status"] = "S"


def sir_recover(a_nodes, G):
    for n in a_nodes:
        if G.nodes[n]["status"] == "I":
            if random.uniform(0, 1) < get_rec(n, G):
                G.nodes[n]["status"] = "R"
