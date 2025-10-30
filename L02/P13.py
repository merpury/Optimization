def est_prob(counting):
    sum_conuting = sum(counting)
    prob_counting = []

    for data in counting:
        prob_data = data/sum_conuting
        prob_counting.append(prob_data)

    return prob_counting