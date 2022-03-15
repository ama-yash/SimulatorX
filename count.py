import networkx as nx
def count_all_si(G):
    status = nx.get_node_attributes(G,'status')
    ethnicity = nx.get_node_attributes(G,'ethnicity')
    gender = nx.get_node_attributes(G,'gender')
    age = nx.get_node_attributes(G,'age')

    inf_nodes = [key for key in status.keys() if status[key] == 'I']
    sus_nodes = [key for key in status.keys() if status[key] == 'S']
    
    white_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 0]
    black_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 1]
    asian_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 2]
    other_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 3]

    male_nodes = [key for key in gender.keys() if gender[key] == 0]
    female_nodes = [key for key in gender.keys() if gender[key] == 1]

    child_nodes = [key for key in age.keys() if age[key] >= 0 and age[key] <= 14]
    adult_nodes = [key for key in age.keys() if age[key] >= 15 and age[key] <= 54]
    senior_nodes = [key for key in age.keys() if age[key] >= 55 and age[key] <= 110]

    data = {
        "total_inf": len(inf_nodes),
        "total_sus": len(sus_nodes),
        "white_inf": len(list(set(inf_nodes) & set(white_nodes))),
        "white_sus": len(list(set(sus_nodes) & set(white_nodes))),
        "black_inf": len(list(set(inf_nodes) & set(black_nodes))),
        "black_sus": len(list(set(sus_nodes) & set(black_nodes))),
        "asian_inf": len(list(set(inf_nodes) & set(asian_nodes))),
        "asian_sus": len(list(set(sus_nodes) & set(asian_nodes))),
        "other_inf": len(list(set(inf_nodes) & set(other_nodes))),
        "other_sus": len(list(set(sus_nodes) & set(other_nodes))),
        "male_sus": len(list(set(sus_nodes) & set(male_nodes))),
        "male_inf": len(list(set(inf_nodes) & set(male_nodes))),
        "female_sus": len(list(set(sus_nodes) & set(female_nodes))),
        "female_inf": len(list(set(inf_nodes) & set(female_nodes))),
        "child_inf": len(list(set(inf_nodes) & set(child_nodes))),
        "child_sus": len(list(set(sus_nodes) & set(child_nodes))),
        "adult_inf": len(list(set(inf_nodes) & set(adult_nodes))),
        "adult_sus": len(list(set(sus_nodes) & set(adult_nodes))),
        "senior_inf": len(list(set(inf_nodes) & set(senior_nodes))),
        "senior_sus": len(list(set(sus_nodes) & set(senior_nodes))),
    }
    return data

def count_all_sir(G):
    status = nx.get_node_attributes(G,'status')
    ethnicity = nx.get_node_attributes(G,'ethnicity')
    gender = nx.get_node_attributes(G,'gender')
    age = nx.get_node_attributes(G,'age')

    inf_nodes = [key for key in status.keys() if status[key] == 'I']
    sus_nodes = [key for key in status.keys() if status[key] == 'S']
    rec_nodes = [key for key in status.keys() if status[key] == 'R']

    white_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 0]
    black_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 1]
    asian_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 2]
    other_nodes = [key for key in ethnicity.keys() if ethnicity[key] == 3]

    male_nodes = [key for key in gender.keys() if gender[key] == 0]
    female_nodes = [key for key in gender.keys() if gender[key] == 1]

    child_nodes = [key for key in age.keys() if age[key] >= 0 and age[key] <= 14]
    adult_nodes = [key for key in age.keys() if age[key] >= 15 and age[key] <= 54]
    senior_nodes = [key for key in age.keys() if age[key] >= 55 and age[key] <= 110]

    data = {
        "total_inf": len(inf_nodes),
        "total_sus": len(sus_nodes),
        "total_rec": len(rec_nodes),
        "white_inf": len(list(set(inf_nodes) & set(white_nodes))),
        "white_sus": len(list(set(sus_nodes) & set(white_nodes))),
        "white_rec": len(list(set(rec_nodes) & set(white_nodes))),
        "black_inf": len(list(set(inf_nodes) & set(black_nodes))),
        "black_sus": len(list(set(sus_nodes) & set(black_nodes))),
        "black_rec": len(list(set(rec_nodes) & set(black_nodes))),
        "asian_inf": len(list(set(inf_nodes) & set(asian_nodes))),
        "asian_sus": len(list(set(sus_nodes) & set(asian_nodes))),
        "asian_rec": len(list(set(rec_nodes) & set(asian_nodes))),
        "other_inf": len(list(set(inf_nodes) & set(other_nodes))),
        "other_sus": len(list(set(sus_nodes) & set(other_nodes))),
        "other_rec": len(list(set(rec_nodes) & set(other_nodes))),
        "male_sus": len(list(set(sus_nodes) & set(male_nodes))),
        "male_inf": len(list(set(inf_nodes) & set(male_nodes))),
        "male_rec": len(list(set(rec_nodes) & set(male_nodes))),
        "female_sus": len(list(set(sus_nodes) & set(female_nodes))),
        "female_inf": len(list(set(inf_nodes) & set(female_nodes))),
        "female_rec": len(list(set(rec_nodes) & set(female_nodes))),
        "child_inf": len(list(set(inf_nodes) & set(child_nodes))),
        "child_sus": len(list(set(sus_nodes) & set(child_nodes))),
        "child_rec": len(list(set(rec_nodes) & set(child_nodes))),
        "adult_inf": len(list(set(inf_nodes) & set(adult_nodes))),
        "adult_sus": len(list(set(sus_nodes) & set(adult_nodes))),
        "adult_rec": len(list(set(rec_nodes) & set(adult_nodes))),
        "senior_inf": len(list(set(inf_nodes) & set(senior_nodes))),
        "senior_sus": len(list(set(sus_nodes) & set(senior_nodes))),
        "senior_rec": len(list(set(rec_nodes) & set(senior_nodes)))
    }
    return data