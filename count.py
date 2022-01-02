def count_all_si(G):
    nodes = len(G.nodes)
    total_inf_count = 0
    total_sus_count = 0
    white_inf_count = 0
    white_sus_count = 0
    black_inf_count = 0
    black_sus_count = 0
    asian_inf_count = 0
    asian_sus_count = 0
    other_inf_count = 0
    other_sus_count = 0
    male_inf_count = 0
    female_inf_count = 0
    male_sus_count = 0
    female_sus_count = 0
    child_inf_count = 0
    child_sus_count = 0
    adult_inf_count = 0
    adult_sus_count = 0
    senior_inf_count = 0
    senior_sus_count = 0
    for node in range(0,nodes):
        if G.nodes[node]['status'] == 'I':
            total_inf_count += 1
            if G.nodes[node]['ethnicity'] == 0:
                white_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 1:
                black_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 2:
                asian_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 3:
                other_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
        elif G.nodes[node]['status'] == 'S':
            total_sus_count += 1
            if G.nodes[node]['ethnicity'] == 0:
                white_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            elif G.nodes[node]['ethnicity'] == 1:
                black_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            if G.nodes[node]['ethnicity'] == 2:
                asian_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            if G.nodes[node]['ethnicity'] == 3:
                other_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
    data = {
        'total_inf':total_inf_count,
        'total_sus':total_sus_count,
        'white_inf' : white_inf_count,
        'white_sus' : white_sus_count,
        'black_inf' : black_inf_count,
        'black_sus' : black_sus_count,
        'asian_inf' : asian_inf_count,
        'asian_sus' : asian_sus_count,
        'other_inf' : other_inf_count,
        'other_sus' : other_sus_count,
        'male_sus': male_sus_count,
        'male_inf': male_inf_count,
        'female_sus': female_sus_count,
        'female_inf': female_inf_count,
        'child_inf':child_inf_count,
        'child_sus':child_sus_count,
        'adult_inf':adult_inf_count,
        'adult_sus':adult_sus_count,
        'senior_inf':senior_inf_count,
        'senior_sus':senior_sus_count,
    }
    return data
def count_all_sir(G):
    nodes = len(G.nodes)
    total_sus_count = 0
    total_inf_count = 0
    total_rec_count = 0
    white_inf_count = 0
    white_sus_count = 0
    white_rec_count = 0
    black_inf_count = 0
    black_sus_count = 0
    black_rec_count = 0
    asian_inf_count = 0
    asian_rec_count = 0
    asian_sus_count = 0
    other_inf_count = 0
    other_rec_count = 0
    other_sus_count = 0
    male_inf_count = 0
    male_sus_count = 0
    female_inf_count = 0
    female_sus_count = 0
    male_rec_count = 0
    female_rec_count = 0
    child_inf_count = 0
    child_sus_count = 0
    child_rec_count = 0
    adult_inf_count = 0
    adult_sus_count = 0
    adult_rec_count = 0
    senior_inf_count = 0
    senior_rec_count = 0
    senior_sus_count = 0
    for node in range(0,nodes):
        if G.nodes[node]['status'] == 'I':
            total_inf_count += 1
            if G.nodes[node]['ethnicity'] == 0:
                white_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 1:
                black_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 2:
                asian_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
            elif G.nodes[node]['ethnicity'] == 3:
                other_inf_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_inf_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_inf_count += 1
                    else:
                        female_inf_count += 1
        elif G.nodes[node]['status'] == 'R':
            total_rec_count += 1
            if G.nodes[node]['ethnicity'] == 0:
                white_rec_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
            elif G.nodes[node]['ethnicity'] == 1:
                black_rec_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
            if G.nodes[node]['ethnicity'] == 2:
                asian_rec_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
            if G.nodes[node]['ethnicity'] == 3:
                other_rec_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_rec_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_rec_count += 1
                    else:
                        female_rec_count += 1
        elif G.nodes[node]['status'] == 'S':
            total_sus_count += 1
            if G.nodes[node]['ethnicity'] == 0:
                white_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            elif G.nodes[node]['ethnicity'] == 1:
                black_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            if G.nodes[node]['ethnicity'] == 2:
                asian_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
            if G.nodes[node]['ethnicity'] == 3:
                other_sus_count += 1
                if G.nodes[node]['age'] >= 0 and G.nodes[node]['age'] <= 14:
                    child_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 15 and G.nodes[node]['age'] <= 54:
                    adult_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
                elif G.nodes[node]['age'] >= 55 and G.nodes[node]['age'] <= 110:
                    senior_sus_count += 1
                    if G.nodes[node]['gender'] == 0:
                        male_sus_count += 1
                    else:
                        female_sus_count += 1
    data = {
        'total_inf':total_inf_count,
        'total_rec':total_rec_count,
        'white_inf' : white_inf_count,
        'white_rec' : white_rec_count,
        'black_inf' : black_inf_count,
        'black_rec' : black_rec_count,
        'asian_inf' : asian_inf_count,
        'asian_rec' : asian_rec_count,
        'other_inf' : other_inf_count,
        'other_rec' : other_rec_count,
        'male_rec': male_rec_count,
        'male_inf': male_inf_count,
        'female_rec': female_rec_count,
        'female_inf': female_inf_count,
        'child_inf':child_inf_count,
        'child_rec':child_rec_count,
        'adult_inf':adult_inf_count,
        'adult_rec':adult_rec_count,
        'senior_inf':senior_inf_count,
        'senior_rec':senior_rec_count,
        'total_sus':total_sus_count,
        'white_sus':white_sus_count,
        'black_sus':black_sus_count,
        'asian_sus':asian_sus_count,
        'other_sus':other_sus_count,
        'male_sus':male_sus_count,
        'female_sus':female_sus_count,
        'child_sus':child_sus_count,
        'adult_sus':adult_sus_count,
        'senior_sus':senior_sus_count
    }
    return data
