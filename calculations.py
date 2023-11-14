def calculate_weighted_average(stats, weights, cutoff=0):
    sum_attributes = 0
    weight_total = 0
    number_of_decimals = 2

    for key in weights:
        weight = int(weights[key])
        if weight >= cutoff:
            weight_total += weight
            attribute = int(stats[key])

            weighted_attribute = attribute * weight
            sum_attributes += weighted_attribute

    weighted_sum = sum_attributes / weight_total

    return round(weighted_sum, number_of_decimals)
