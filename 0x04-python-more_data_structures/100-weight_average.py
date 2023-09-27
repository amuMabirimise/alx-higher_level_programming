#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    scores, weights = zip(*my_list)
    weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
    total_weight = sum(weights)

    if total_weight == 0:
        return 0
    else:
        return weighted_sum / total_weight
