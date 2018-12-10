#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    import math
    all_errors = []

    for index in range(len(net_worths)):
        err = net_worths[index][0] - predictions[index][0]
        err = math.sqrt(err * err)
        all_errors.append(err)
        data = (ages[index][0], net_worths[index][0], err)
        cleaned_data.append(data)

    limit = (len(net_worths) * len(net_worths) / 100)

    while ((len(cleaned_data) > limit)):
        for a_tuple in cleaned_data:
            max_err = max(all_errors)
            if (a_tuple[2] == max_err and len(cleaned_data) > limit):
                err_index = all_errors.index(max_err)
                all_errors.pop(err_index)

                tuple_index = cleaned_data.index(a_tuple)
                cleaned_data.pop(tuple_index)

    return cleaned_data

