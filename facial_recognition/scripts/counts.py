def count(eth_list, gen_list, age_list):
    n = len(eth_list)
    white_count = 0
    black_count = 0
    asian_count = 0
    other_count = 0
    male_count = 0
    female_count = 0
    child_count = 0
    adult_count = 0
    senior_count = 0
    for e in eth_list:
        if e == 0:
            white_count += 1
        elif e == 1:
            black_count += 1
        elif e == 2:
            asian_count += 1
        else:
            other_count += 1
    for g in gen_list:
        if g == 0:
            male_count += 1
        else:
            female_count += 1
    for a in age_list:
        if a >= 0 and a <= 2:
            child_count += 1
        elif a > 2 and a <= 10:
            adult_count += 1
        else:
            senior_count += 1
    white_ratio = round((white_count * 100) / n, 2)
    black_ratio = round((black_count * 100) / n, 2)
    asian_ratio = round((asian_count * 100) / n, 2)
    other_ratio = round((other_count * 100) / n, 2)
    male_ratio = round((male_count * 100) / n, 2)
    female_ratio = round((female_count * 100) / n, 2)
    child_ratio = round((child_count * 100) / n, 2)
    adult_ratio = round((adult_count * 100) / n, 2)
    senior_ratio = round((senior_count * 100) / n, 2)
    if (white_ratio + black_ratio + asian_ratio + other_ratio) > 100:
        diff = (white_ratio + black_ratio + asian_ratio + other_ratio) - 100
        other_ratio = other_ratio - diff
    elif (white_ratio + black_ratio + asian_ratio + other_ratio) < 100:
        diff = 100 - (white_ratio + black_ratio + asian_ratio + other_ratio)
        other_ratio = other_ratio + diff
    if (male_ratio + female_ratio) > 100:
        diff = (male_ratio + female_ratio) - 100
        female_ratio = female_ratio - diff
    elif (male_ratio + female_ratio) < 100:
        diff = 100 - (male_ratio + female_ratio)
        female_ratio = female_ratio + diff
    if (child_ratio + adult_ratio + senior_ratio) > 100:
        diff = (child_ratio + adult_ratio + senior_ratio) - 100
        senior_ratio = senior_ratio - diff
    elif (child_ratio + adult_ratio + senior_ratio) < 100:
        diff = 100 - (child_ratio + adult_ratio + senior_ratio)
        senior_ratio = senior_ratio + diff
    data = {
        "N": n,
        "white": white_ratio,
        "black": black_ratio,
        "asian": asian_ratio,
        "other": other_ratio,
        "male": male_ratio,
        "female": female_ratio,
        "child": child_ratio,
        "adult": adult_ratio,
        "senior": senior_ratio,
    }
    return data
